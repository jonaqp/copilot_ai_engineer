#!/usr/bin/env python3
import argparse
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HOOK = ROOT / ".github" / "hooks" / "scripts" / "hook_handler.py"

SCENARIOS = [
    ("sessionStart", {"sessionId": "demo-1", "timestamp": 1, "cwd": str(ROOT), "source": "new"}),
    ("userPromptSubmitted", {"sessionId": "demo-1", "timestamp": 2, "cwd": str(ROOT), "prompt": "Agrega una funcion para vaciar el carrito y ejecuta las pruebas"}),
    ("preToolUse", {"sessionId": "demo-1", "timestamp": 3, "cwd": str(ROOT), "toolName": "bash", "toolArgs": {"command": "python -m unittest discover -s demo_cart -p test_*.py"}}),
    ("preToolUse", {"sessionId": "demo-1", "timestamp": 4, "cwd": str(ROOT), "toolName": "bash", "toolArgs": {"command": "rm -rf ."}}),
    ("postToolUse", {"sessionId": "demo-1", "timestamp": 5, "cwd": str(ROOT), "toolName": "edit", "toolArgs": {"path": "demo_cart/cart.py"}, "toolResult": {"resultType": "success", "textResultForLlm": "updated"}}),
    ("postToolUseFailure", {"sessionId": "demo-1", "timestamp": 6, "cwd": str(ROOT), "toolName": "bash", "toolArgs": {"command": "false"}, "error": "exit code 1"}),
    ("subagentStart", {"sessionId": "demo-1", "timestamp": 7, "cwd": str(ROOT), "agentName": "code-review", "agentId": "a1", "agentType": "custom"}),
    ("subagentStop", {"sessionId": "demo-1", "timestamp": 8, "cwd": str(ROOT), "agentName": "code-review", "agentId": "a1", "agentType": "custom", "response": "PASS: las reglas del carrito son claras", "stopReason": "end_turn", "transcriptPath": "demo"}),
    ("preCompact", {"sessionId": "demo-1", "timestamp": 9, "cwd": str(ROOT), "trigger": "manual", "customInstructions": "keep status", "transcriptPath": "demo"}),
    ("notification", {"sessionId": "demo-1", "timestamp": 10, "cwd": str(ROOT), "notification_type": "agent_idle"}),
    ("errorOccurred", {"sessionId": "demo-1", "timestamp": 11, "cwd": str(ROOT), "error": {"message": "demo error", "name": "DemoError"}, "error_context": "tool_execution", "recoverable": True}),
    ("permissionRequest", {"sessionId": "demo-1", "timestamp": 12, "cwd": str(ROOT), "toolName": "bash", "toolArgs": {"command": "python -m unittest"}}),
    ("agentStop", {"sessionId": "demo-1", "timestamp": 13, "cwd": str(ROOT), "transcriptPath": "demo", "stopReason": "end_turn", "stop_hook_active": False}),
    ("sessionEnd", {"sessionId": "demo-1", "timestamp": 14, "cwd": str(ROOT), "reason": "complete"}),
]


def call(event, payload):
    p = subprocess.run([sys.executable, str(HOOK), event], input=json.dumps(payload), text=True, capture_output=True, cwd=ROOT)
    out = p.stdout.strip() or "{}"
    try:
        data = json.loads(out)
    except Exception:
        data = {"raw": out, "stderr": p.stderr.strip(), "returncode": p.returncode}
    return data


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--all", action="store_true")
    parser.add_argument("--event")
    args = parser.parse_args()
    selected = SCENARIOS if args.all or not args.event else [x for x in SCENARIOS if x[0] == args.event]
    for i, (event, payload) in enumerate(selected, 1):
        print(f"[{i:02}] {event}")
        print(json.dumps(call(event, payload), indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
