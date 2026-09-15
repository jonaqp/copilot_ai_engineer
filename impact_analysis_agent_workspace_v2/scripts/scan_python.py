#!/usr/bin/env python3
import argparse, ast, json
from pathlib import Path

p = argparse.ArgumentParser(description="Inventory Python classes, functions and imports")
p.add_argument("path")
args = p.parse_args()
root = Path(args.path)
records = []
for file in sorted(root.rglob("*.py")):
    if any(part.startswith(".") for part in file.parts):
        continue
    try:
        tree = ast.parse(file.read_text(encoding="utf-8"))
    except (SyntaxError, UnicodeDecodeError):
        continue
    classes = [n.name for n in ast.walk(tree) if isinstance(n, ast.ClassDef)]
    functions = [n.name for n in ast.walk(tree) if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef))]
    imports = []
    for n in ast.walk(tree):
        if isinstance(n, ast.Import): imports += [a.name for a in n.names]
        elif isinstance(n, ast.ImportFrom) and n.module: imports.append(n.module)
    records.append({"file": str(file.relative_to(root)), "classes": classes, "functions": functions, "imports": sorted(set(imports))})
print(json.dumps(records, indent=2, ensure_ascii=False))
