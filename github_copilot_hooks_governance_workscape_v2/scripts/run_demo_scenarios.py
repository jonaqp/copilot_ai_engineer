#!/usr/bin/env python3
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HOOK = ROOT / ".github" / "hooks" / "scripts" / "hook_handler.py"


def invoke(event, payload):
    p = subprocess.run([sys.executable, str(HOOK), event], input=json.dumps(payload), text=True, capture_output=True, cwd=ROOT)
    return json.loads(p.stdout or "{}")


def main():
    safe = invoke("preToolUse", {"toolName": "bash", "toolArgs": {"command": "python -m unittest discover -s demo_app"}})
    dangerous = invoke("preToolUse", {"toolName": "bash", "toolArgs": {"command": "rm -rf ."}})
    secret = invoke("preToolUse", {"toolName": "bash", "toolArgs": {"command": "echo token=ghp_123456789012345678901234567890"}})
    stop = invoke("agentStop", {"stop_hook_active": False})

    print("SAFE TOOL      :", safe.get("permissionDecision"))
    print("DANGEROUS TOOL :", dangerous.get("permissionDecision"))
    print("SECRET TOOL    :", secret.get("permissionDecision"))
    print("AGENT STOP     :", stop.get("decision"))

    ok = safe.get("permissionDecision") == "allow" and dangerous.get("permissionDecision") == "deny" and secret.get("permissionDecision") == "deny" and stop.get("decision") == "allow"
    print("RESULT         :", "PASS" if ok else "FAIL")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
