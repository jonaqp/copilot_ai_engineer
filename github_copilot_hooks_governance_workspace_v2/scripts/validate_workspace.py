#!/usr/bin/env python3
import json
import py_compile
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
checks = []

def check(name, cond, detail=''):
    checks.append((name, bool(cond), detail))

# JSON configs
for path in sorted((ROOT / '.github' / 'hooks').glob('*.json')):
    try:
        data = json.loads(path.read_text(encoding='utf-8'))
        check(f'json:{path.name}', isinstance(data.get('hooks'), dict) and bool(data['hooks']))
    except Exception as e:
        check(f'json:{path.name}', False, str(e))

# Layout clarity
required = [
    ROOT / '.github/hooks/README.md',
    ROOT / '.github/hooks/01-session-audit.json',
    ROOT / '.github/hooks/02-tool-guardrails.json',
    ROOT / '.github/hooks/03-agent-lifecycle.json',
    ROOT / '.github/hooks/scripts/hook_handler.py',
    ROOT / 'demo_cart/cart.py',
    ROOT / 'demo_cart/test_cart.py',
]
for path in required:
    check(f'archivo:{path.relative_to(ROOT)}', path.exists())

# Python syntax
for path in list((ROOT / 'scripts').glob('*.py')) + list((ROOT / '.github/hooks/scripts').glob('*.py')) + list((ROOT / 'demo_cart').glob('*.py')):
    try:
        py_compile.compile(str(path), doraise=True)
        check(f'python:{path.relative_to(ROOT)}', True)
    except Exception as e:
        check(f'python:{path.relative_to(ROOT)}', False, str(e))

# Demo tests
p = subprocess.run([sys.executable, '-m', 'unittest', 'discover', '-s', 'demo_cart', '-p', 'test_*.py'], cwd=ROOT, capture_output=True, text=True)
check('carrito-tests', p.returncode == 0, (p.stdout+p.stderr)[-500:])

# Functional demo
p = subprocess.run([sys.executable, 'demo_cart/demo.py'], cwd=ROOT, capture_output=True, text=True)
check('carrito-demo', p.returncode == 0 and 'APPROVED' in p.stdout, (p.stdout+p.stderr)[-500:])

# Hook scenarios
p = subprocess.run([sys.executable, 'scripts/run_demo_scenarios.py'], cwd=ROOT, capture_output=True, text=True)
check('hook-scenarios', p.returncode == 0 and 'PASS' in p.stdout, (p.stdout+p.stderr)[-700:])

for name, ok, detail in checks:
    print(f"{'PASS' if ok else 'FAIL'}: {name}" + (f' :: {detail.strip()}' if detail and not ok else ''))
failed = [x for x in checks if not x[1]]
print(f"\nRESULTADO: {'PASS' if not failed else 'FAIL'} ({len(checks)-len(failed)}/{len(checks)})")
raise SystemExit(1 if failed else 0)
