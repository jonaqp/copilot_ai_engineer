#!/usr/bin/env python3
import json
import os
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
LOG_DIR = ROOT / ".github" / "hooks" / "logs"
LOG_DIR.mkdir(parents=True, exist_ok=True)
AUDIT_LOG = LOG_DIR / "audit.jsonl"

DANGEROUS_PATTERNS = [
    r"\brm\s+-rf\s+[/~.]",
    r"\bmkfs\b",
    r"\bshutdown\b",
    r"\breboot\b",
    r"\bformat\s+[a-zA-Z]:",
    r"\bcat\s+.*(?:id_rsa|credentials|\.env)",
    r"\bprintenv\b",
    r"\benv\s*$",
]

SECRET_PATTERNS = [
    r"(?i)(api[_-]?key|token|password|secret)\s*[=:]\s*['\"]?[A-Za-z0-9_\-]{8,}",
    r"gh[pousr]_[A-Za-z0-9]{20,}",
]


def read_payload():
    raw = sys.stdin.read().strip()
    if not raw:
        return {}
    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        return {"_raw": raw, "_parse_error": True}


def audit(event, payload, outcome="observed", detail=None):
    record = {
        "ts": datetime.now(timezone.utc).isoformat(),
        "event": event,
        "outcome": outcome,
        "sessionId": payload.get("sessionId") or payload.get("session_id"),
        "toolName": payload.get("toolName") or payload.get("tool_name"),
        "detail": detail,
    }
    with AUDIT_LOG.open("a", encoding="utf-8") as f:
        f.write(json.dumps(record, ensure_ascii=False) + "\n")


def tool_text(payload):
    args = payload.get("toolArgs", payload.get("tool_input", {}))
    if isinstance(args, str):
        return args
    return json.dumps(args, ensure_ascii=False)


def has_secret(text):
    return any(re.search(p, text or "") for p in SECRET_PATTERNS)


def handle_session_start(payload):
    audit("sessionStart", payload, "allow", "Sesion inicializada")
    return {"additionalContext": "Laboratorio de hooks activo: solo local, auditable y con operaciones destructivas bloqueadas."}


def handle_prompt(payload):
    prompt = payload.get("prompt", "")
    detail = "se detecto texto con apariencia de secreto" if has_secret(prompt) else "prompt auditado"
    audit("userPromptSubmitted", payload, "observed", detail)
    return {}


def handle_pre_tool(payload):
    name = payload.get("toolName") or payload.get("tool_name") or "unknown"
    text = tool_text(payload)
    lowered = text.lower()

    if has_secret(text):
        reason = "Bloqueado: los argumentos de la herramienta parecen contener una credencial o secreto."
        audit("preToolUse", payload, "deny", reason)
        return {"permissionDecision": "deny", "permissionDecisionReason": reason}

    if any(re.search(p, text, re.IGNORECASE) for p in DANGEROUS_PATTERNS):
        reason = "Bloqueado: se detecto un comando destructivo o que podria exponer credenciales."
        audit("preToolUse", payload, "deny", reason)
        return {"permissionDecision": "deny", "permissionDecisionReason": reason}

    if name in {"edit", "create", "Write", "Edit"} and ("../" in text or "..\\" in text):
        reason = "Bloqueado: esta demo no permite escribir fuera de los limites del repositorio."
        audit("preToolUse", payload, "deny", reason)
        return {"permissionDecision": "deny", "permissionDecisionReason": reason}

    # Demonstrate argument rewriting for a harmless shell command.
    if name in {"bash", "powershell", "Bash"} and "pytest -q" in lowered:
        audit("preToolUse", payload, "allow", "Comando de pruebas permitido")
        return {"permissionDecision": "allow"}

    audit("preToolUse", payload, "allow", f"Herramienta permitida: {name}")
    return {"permissionDecision": "allow"}


def handle_post_tool(payload):
    name = payload.get("toolName") or payload.get("tool_name") or "unknown"
    audit("postToolUse", payload, "observed", f"Herramienta completada: {name}")
    if name in {"edit", "create", "Edit", "Write"}:
        return {"additionalContext": "Se modifico un archivo. Ejecuta pruebas focalizadas antes de declarar la tarea terminada."}
    return {}


def handle_post_tool_failure(payload):
    err = payload.get("error", "tool failed")
    audit("postToolUseFailure", payload, "failure", str(err)[:300])
    return {"additionalContext": "La ejecucion de la herramienta fallo. Revisa el error, cambia la estrategia y evita reintentos ciegos."}


def handle_subagent_start(payload):
    name = payload.get("agentName") or payload.get("agent_name") or "subagent"
    audit("subagentStart", payload, "observed", f"Iniciado {name}")
    return {"additionalContext": "Mantente dentro del alcance del repositorio y devuelve evidencia concisa con conclusiones PASS/FAIL."}


def handle_subagent_stop(payload):
    response = payload.get("response") or payload.get("last_assistant_message") or ""
    audit("subagentStop", payload, "allow", "Resultado del subagente inspeccionado")
    if has_secret(response):
        return {
            "decision": "allow",
            "modifiedResponse": "[REDACTADO POR HOOK] La salida del subagente contenia material con apariencia de secreto y fue ocultada."
        }
    return {"decision": "allow"}


def run_quality_gate():
    cmd = [sys.executable, "-m", "unittest", "discover", "-s", "demo_app", "-p", "test_*.py"]
    proc = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True, timeout=15)
    return proc.returncode == 0, (proc.stdout + proc.stderr)[-1200:]


def handle_agent_stop(payload):
    already_active = bool(payload.get("stop_hook_active"))
    ok, output = run_quality_gate()
    audit("agentStop", payload, "allow" if ok else "block", "quality gate superado" if ok else "quality gate fallido")
    if ok:
        return {"decision": "allow"}
    if already_active:
        return {"decision": "allow"}
    return {
        "decision": "block",
        "reason": "Final quality gate fallido. Fix the demo_app unit tests before ending the turn. Test output:\n" + output
    }


def handle_error(payload):
    err = payload.get("error", {})
    audit("errorOccurred", payload, "error", str(err)[:500])
    return {}


def handle_session_end(payload):
    audit("sessionEnd", payload, "observed", f"reason={payload.get('reason', 'unknown')}")
    return {}


def handle_notification(payload):
    audit("notification", payload, "observed", str(payload.get("notification_type", payload.get("notificationType", "unknown"))))
    return {}


def handle_pre_compact(payload):
    audit("preCompact", payload, "observed", f"trigger={payload.get('trigger', 'unknown')}")
    return {"additionalContext": "Conserva la tarea actual, los checks fallidos y las decisiones de hooks durante la compactacion."}


def handle_permission_request(payload):
    name = payload.get("toolName") or payload.get("tool_name") or "unknown"
    text = tool_text(payload)
    if any(re.search(p, text, re.IGNORECASE) for p in DANGEROUS_PATTERNS) or has_secret(text):
        audit("permissionRequest", payload, "deny", f"Permiso denegado para {name}")
        return {"behavior": "deny", "message": "La politica del hook denego esta operacion sensible.", "interrupt": False}
    audit("permissionRequest", payload, "allow", f"Permiso permitido para {name}")
    return {"behavior": "allow"}


HANDLERS = {
    "sessionStart": handle_session_start,
    "userPromptSubmitted": handle_prompt,
    "preToolUse": handle_pre_tool,
    "postToolUse": handle_post_tool,
    "postToolUseFailure": handle_post_tool_failure,
    "subagentStart": handle_subagent_start,
    "subagentStop": handle_subagent_stop,
    "agentStop": handle_agent_stop,
    "errorOccurred": handle_error,
    "sessionEnd": handle_session_end,
    "notification": handle_notification,
    "preCompact": handle_pre_compact,
    "permissionRequest": handle_permission_request,
}


def main():
    if len(sys.argv) != 2 or sys.argv[1] not in HANDLERS:
        print(json.dumps({"error": "uso: hook_handler.py <evento>"}))
        return 1
    event = sys.argv[1]
    payload = read_payload()
    result = HANDLERS[event](payload)
    if result:
        print(json.dumps(result, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
