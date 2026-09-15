#!/usr/bin/env python3
"""Renderiza una plantilla APX aprobada sin inventar APIs propietarias.

Sustituye placeholders exactos {{CLAVE}} en nombres y contenidos de archivos.
No descarga plantillas, no ejecuta builds y no sobrescribe salvo --overwrite.
"""
import argparse
import json
import re
import shutil
from pathlib import Path

TOKEN = re.compile(r"\{\{([A-Z0-9_]+)\}\}")


def substitute(text: str, params: dict[str, str]) -> str:
    def repl(match: re.Match[str]) -> str:
        key = match.group(1)
        if key not in params:
            raise KeyError(f"Falta parametro para placeholder: {key}")
        return str(params[key])
    return TOKEN.sub(repl, text)


def main() -> None:
    parser = argparse.ArgumentParser(description="Renderiza una plantilla APX previamente aprobada")
    parser.add_argument("--template-dir", required=True, help="Directorio de plantilla aprobada")
    parser.add_argument("--params", required=True, help="JSON con valores de placeholders")
    parser.add_argument("--output-dir", required=True, help="Directorio destino")
    parser.add_argument("--overwrite", action="store_true", help="Permitir sobrescritura de archivos existentes")
    args = parser.parse_args()

    template_dir = Path(args.template_dir).resolve()
    output_dir = Path(args.output_dir).resolve()
    if not template_dir.is_dir():
        raise SystemExit(f"Template inexistente: {template_dir}")
    params = json.loads(Path(args.params).read_text(encoding="utf-8"))
    if not isinstance(params, dict) or not all(isinstance(k, str) for k in params):
        raise SystemExit("--params debe contener un objeto JSON")

    rendered: list[str] = []
    for source in sorted(template_dir.rglob("*")):
        rel = source.relative_to(template_dir)
        rel_parts = [substitute(part, params) for part in rel.parts]
        target = output_dir.joinpath(*rel_parts)
        if source.is_dir():
            target.mkdir(parents=True, exist_ok=True)
            continue
        target.parent.mkdir(parents=True, exist_ok=True)
        if target.exists() and not args.overwrite:
            raise SystemExit(f"Destino ya existe; usar --overwrite si corresponde: {target}")
        raw = source.read_bytes()
        try:
            text = raw.decode("utf-8")
        except UnicodeDecodeError:
            shutil.copy2(source, target)
        else:
            target.write_text(substitute(text, params), encoding="utf-8")
        rendered.append(str(target))

    print(json.dumps({
        "status": "rendered",
        "template": str(template_dir),
        "output": str(output_dir),
        "files": rendered,
        "guardrail": "La validez APX depende de que la plantilla origen haya sido homologada/aprobada."
    }, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
