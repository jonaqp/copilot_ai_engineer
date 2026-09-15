#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LOG = ROOT / ".github" / "hooks" / "logs" / "hook-trace.jsonl"

if not LOG.exists():
    print("No hay traza. Ejecuta primero: python scripts/simular_prompt.py \"tu prompt\"")
    raise SystemExit(0)

print("HOOK | RESULTADO | EXPLICACION")
print("-" * 90)
for line in LOG.read_text(encoding="utf-8").splitlines():
    item = json.loads(line)
    print(f"{item['hook']:<20} | {item['outcome']:<9} | {item['explicacion']}")
