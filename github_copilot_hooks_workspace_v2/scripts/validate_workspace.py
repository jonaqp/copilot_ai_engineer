#!/usr/bin/env python3
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
checks = []

def add(name, ok):
    checks.append((name, bool(ok)))
    print(("PASS" if ok else "FAIL") + ": " + name)

# JSON valido
cfg = ROOT / ".github" / "hooks" / "hooks-explicador.json"
try:
    data = json.loads(cfg.read_text(encoding="utf-8"))
    add("JSON de hooks valido", data.get("version") == 1 and "hooks" in data)
except Exception:
    add("JSON de hooks valido", False)

# Archivos clave
for rel in [
    ".github/agents/hooks-explicador.agent.md",
    ".github/hooks/scripts/hook_explicador.py",
    "demo/accion_demo.py",
    "scripts/simular_prompt.py",
    "scripts/ver_traza.py",
]:
    add(f"Existe {rel}", (ROOT / rel).exists())

# Sintaxis Python
pyfiles = list(ROOT.rglob("*.py"))
proc = subprocess.run([sys.executable, "-m", "py_compile", *map(str, pyfiles)], capture_output=True, text=True)
add("Sintaxis Python", proc.returncode == 0)

# Simulacion
proc = subprocess.run([sys.executable, "scripts/simular_prompt.py", "hola hooks"], cwd=ROOT, capture_output=True, text=True)
add("Simulacion de prompt", proc.returncode == 0 and "preToolUse" in proc.stdout and "agentStop" in proc.stdout)

# Bloqueo de comando peligroso
hook = ROOT / ".github" / "hooks" / "scripts" / "hook_explicador.py"
payload = json.dumps({"toolName": "bash", "toolArgs": {"command": "rm -rf ."}})
proc = subprocess.run([sys.executable, str(hook), "preToolUse"], input=payload, text=True, capture_output=True, cwd=ROOT)
add("preToolUse bloquea comando peligroso", '"deny"' in proc.stdout)

passed = sum(ok for _, ok in checks)
result = "PASS" if passed == len(checks) else "FAIL"
report = ["# Validation Report", "", f"Resultado: **{result}** ({passed}/{len(checks)})", ""]
report += [f"- {'PASS' if ok else 'FAIL'}: {name}" for name, ok in checks]
(ROOT / "VALIDATION_REPORT.md").write_text("\n".join(report) + "\n", encoding="utf-8")
print(f"RESULTADO: {result} ({passed}/{len(checks)})")
raise SystemExit(0 if result == "PASS" else 1)
