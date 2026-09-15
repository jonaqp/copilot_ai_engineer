#!/usr/bin/env python3
import json
import py_compile
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
checks = []

def check(name, cond, detail=""):
    checks.append((name, bool(cond), detail))

# JSON
for path in (ROOT / ".github" / "hooks").glob("*.json"):
    try:
        json.loads(path.read_text(encoding="utf-8"))
        check(f"json:{path.name}", True)
    except Exception as e:
        check(f"json:{path.name}", False, str(e))

# Python syntax
for path in list((ROOT / "scripts").glob("*.py")) + list((ROOT / ".github" / "hooks" / "scripts").glob("*.py")) + list((ROOT / "demo_app").glob("*.py")):
    try:
        py_compile.compile(str(path), doraise=True)
        check(f"python:{path.relative_to(ROOT)}", True)
    except Exception as e:
        check(f"python:{path.relative_to(ROOT)}", False, str(e))

# Tests
p = subprocess.run([sys.executable, "-m", "unittest", "discover", "-s", "demo_app", "-p", "test_*.py"], cwd=ROOT, capture_output=True, text=True)
check("demo-tests", p.returncode == 0, (p.stdout + p.stderr)[-400:])

# Scenarios
p = subprocess.run([sys.executable, "scripts/run_demo_scenarios.py"], cwd=ROOT, capture_output=True, text=True)
check("hook-scenarios", p.returncode == 0, (p.stdout + p.stderr)[-600:])

for name, ok, detail in checks:
    print(f"{'PASS' if ok else 'FAIL'}: {name}" + (f" :: {detail.strip()}" if detail and not ok else ""))

failed = [x for x in checks if not x[1]]
print(f"\nRESULT: {'PASS' if not failed else 'FAIL'} ({len(checks)-len(failed)}/{len(checks)})")
raise SystemExit(1 if failed else 0)
