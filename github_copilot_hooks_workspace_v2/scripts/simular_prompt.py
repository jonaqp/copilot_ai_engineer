#!/usr/bin/env python3
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HOOK = ROOT / ".github" / "hooks" / "scripts" / "hook_explicador.py"


def call(event, payload):
    p = subprocess.run(
        [sys.executable, str(HOOK), event],
        input=json.dumps(payload), text=True, capture_output=True, cwd=ROOT
    )
    return p.stdout.strip()


def show(n, event, purpose, output=""):
    print(f"{n}. {event}")
    print(f"   Que hace: {purpose}")
    if output:
        print(f"   Salida: {output}")


def main():
    prompt = " ".join(sys.argv[1:]).strip() or "Hola, explica que haces"
    log = ROOT / ".github" / "hooks" / "logs" / "hook-trace.jsonl"
    if log.exists():
        log.unlink()

    out = call("sessionStart", {"sessionId": "demo-001"})
    show(1, "sessionStart", "Inicializa la sesion.", out)

    out = call("userPromptSubmitted", {"sessionId": "demo-001", "prompt": prompt})
    show(2, "userPromptSubmitted", "Observa el prompt enviado por el usuario.", out)

    command = f"{sys.executable} demo/accion_demo.py"
    out = call("preToolUse", {"sessionId": "demo-001", "toolName": "bash", "toolArgs": {"command": command}})
    show(3, "preToolUse", "Decide si la herramienta puede ejecutarse.", out)

    tool = subprocess.run([sys.executable, "demo/accion_demo.py"], cwd=ROOT, capture_output=True, text=True)
    print("4. TOOL")
    print("   Que hace: ejecuta una accion local inocua.")
    print("   Salida:", tool.stdout.strip().replace("\n", " | "))

    if tool.returncode == 0:
        out = call("postToolUse", {"sessionId": "demo-001", "toolName": "bash", "toolResult": tool.stdout})
        show(5, "postToolUse", "Registra que la herramienta termino bien.", out)
    else:
        out = call("postToolUseFailure", {"sessionId": "demo-001", "toolName": "bash", "error": tool.stderr})
        show(5, "postToolUseFailure", "Registra el error de una herramienta.", out)

    out = call("agentStop", {"sessionId": "demo-001"})
    show(6, "agentStop", "Decide si el agente puede finalizar.", out)

    out = call("sessionEnd", {"sessionId": "demo-001", "reason": "demo complete"})
    show(7, "sessionEnd", "Cierra la sesion y deja evidencia.", out)

    print("\nPROMPT SIMULADO:", prompt)
    print("TRAZA:", log)


if __name__ == "__main__":
    main()
