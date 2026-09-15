#!/usr/bin/env python3
import argparse, json
from pathlib import Path

p = argparse.ArgumentParser(description="Validate architecture graph JSON")
p.add_argument("graph")
args = p.parse_args()
data = json.loads(Path(args.graph).read_text(encoding="utf-8"))
ids = [c["id"] for c in data.get("components", [])]
errors = []
if len(ids) != len(set(ids)):
    errors.append("duplicate component ids")
known = set(ids)
for i, dep in enumerate(data.get("dependencies", []), 1):
    if dep.get("source") not in known or dep.get("target") not in known:
        errors.append(f"edge {i} references unknown component")
if errors:
    for e in errors: print("ERROR:", e)
    raise SystemExit(1)
print(f"PASS: {len(ids)} components, {len(data.get('dependencies', []))} dependencies")
