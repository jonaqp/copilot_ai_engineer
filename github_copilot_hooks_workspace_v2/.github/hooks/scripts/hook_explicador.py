#!/usr/bin/env python3
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
LOG = ROOT / ".github" / "hooks" / "logs" / "hook-trace.jsonl"
LOG.parent.mkdir(parents=True, exist_ok=True)

DANGEROUS = [
    r"\brm\s+-rf\b",
    r"\bshutdown\b",
    r"\breboot\b",
    r"\bformat\s+[a-zA-Z]:",
]

EXPLANATIONS = {
    "sessionStart": "Se inicio o reanudo la sesion del agente.",
    "userPromptSubmitted": "El usuario envio un prompt y el hook lo observo antes de continuar.",
    "preToolUse": "Copilot esta a punto de usar una herramienta. Este hook puede permitirla o bloquearla.",
    "postToolUse": "La herramienta termino correctamente y el hook puede registrar o agregar contexto.",
    "postToolUseFailure": "La herramienta fallo. El hook permite registrar el error y orientar la recuperacion.",
    "agentStop": "El agente intenta terminar. Este hook puede permitir el cierre o bloquearlo si falta una validacion.",
    "sessionEnd": "La sesion termino y el hook puede cerrar auditoria o limpiar recursos."
}


def read_payload():
    raw = sys.stdin.read().strip()
    if not raw:
        return {}
    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        return {"_raw": raw}


def tool_text(payload):
    args = payload.get("toolArgs", payload.get("tool_input", {}))
    if isinstance(args, str):
        return args
    return json.dumps(args, ensure_ascii=False)


def log_event(event, payload, outcome="observed", detail=""):
    record = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "hook": event,
        "outcome": outcome,
        "tool": payload.get("toolName") or payload.get("tool_name"),
        "explicacion": EXPLANATIONS[event],
        "detalle": detail
    }
    with LOG.open("a", encoding="utf-8") as f:
        f.write(json.dumps(record, ensure_ascii=False) + "\n")


def main():
    if len(sys.argv) != 2 or sys.argv[1] not in EXPLANATIONS:
        print(json.dumps({"error": "Uso: hook_explicador.py <evento>"}, ensure_ascii=False))
        return 1

    event = sys.argv[1]
    payload = read_payload()

    if event == "preToolUse":
        text = tool_text(payload)
        if any(re.search(p, text, re.IGNORECASE) for p in DANGEROUS):
            detail = "Operacion bloqueada por la demo educativa."
            log_event(event, payload, "deny", detail)
            print(json.dumps({
                "permissionDecision": "deny",
                "permissionDecisionReason": "Hook preToolUse: comando potencialmente destructivo bloqueado."
            }, ensure_ascii=False))
            return 0
        log_event(event, payload, "allow", "Operacion local permitida.")
        print(json.dumps({
            "permissionDecision": "allow",
            "permissionDecisionReason": "Hook preToolUse: la operacion demo es segura."
        }, ensure_ascii=False))
        return 0

    if event == "postToolUseFailure":
        log_event(event, payload, "failure", str(payload.get("error", "tool failure"))[:250])
        print(json.dumps({
            "additionalContext": "El hook postToolUseFailure detecto un fallo. Revisar el error antes de reintentar."
        }, ensure_ascii=False))
        return 0

    if event == "postToolUse":
        log_event(event, payload, "success", "La tool termino correctamente.")
        print(json.dumps({
            "additionalContext": "Hook postToolUse ejecutado: la herramienta termino correctamente."
        }, ensure_ascii=False))
        return 0

    if event == "agentStop":
        log_event(event, payload, "allow", "Demo sin validaciones pendientes.")
        print(json.dumps({"decision": "allow"}, ensure_ascii=False))
        return 0

    log_event(event, payload)
    if event == "sessionStart":
        print(json.dumps({"additionalContext": "Demo simple de hooks activa. Explica los hooks en espanol."}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
