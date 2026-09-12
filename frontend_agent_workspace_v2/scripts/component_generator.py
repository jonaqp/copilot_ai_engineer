#!/usr/bin/env python3
import argparse
from pathlib import Path
import shutil
import sys

TEMPLATES = {
    "panel": "panel-standard.html",
    "table": "table-standard.html",
    "form": "form-standard.html",
    "layout": "layout-standard.html",
}


def repo_root() -> Path:
    return Path(__file__).resolve().parent.parent


def generate_component(component_type: str, output_path: str) -> int:
    root = repo_root()
    source = root / "reference-standards" / TEMPLATES[component_type]
    target = Path(output_path).expanduser().resolve()

    if not source.exists():
        print(f"ERROR: No existe la referencia: {source}")
        return 2

    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(source, target)
    print(f"PASS: plantilla '{component_type}' generada en {target}")
    print(f"SOURCE: {source}")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Genera componentes desde referencias Front-End locales.")
    parser.add_argument("--type", required=True, choices=sorted(TEMPLATES), help="Tipo de componente")
    parser.add_argument("--output", required=True, help="Ruta de salida HTML")
    args = parser.parse_args()
    return generate_component(args.type, args.output)


if __name__ == "__main__":
    sys.exit(main())
