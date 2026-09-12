#!/usr/bin/env python3
import argparse
from html.parser import HTMLParser
from pathlib import Path
import re
import sys


class AuditParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.classes = []
        self.inline_styles = []
        self.tables = []
        self._table = None
        self.images_without_alt = []
        self.icon_buttons_without_name = []
        self.external_css = []

    def handle_starttag(self, tag, attrs):
        data = dict(attrs)
        if "class" in data:
            self.classes.extend(data["class"].split())
        if "style" in data:
            self.inline_styles.append(tag)
        if tag == "link" and data.get("rel") == "stylesheet":
            href = data.get("href", "")
            if href.startswith(("http://", "https://", "//")):
                self.external_css.append(href)
        if tag == "img" and "alt" not in data:
            self.images_without_alt.append(data.get("src", "<sin src>"))
        if tag == "table":
            self._table = {"caption": False, "ths": []}
            self.tables.append(self._table)
        elif tag == "caption" and self._table is not None:
            self._table["caption"] = True
        elif tag == "th" and self._table is not None:
            self._table["ths"].append(data.get("scope"))
        elif tag == "button":
            has_name = bool(data.get("aria-label") or data.get("title"))
            classes = data.get("class", "").split()
            if "ux-local-btn-icon" in classes and not has_name:
                self.icon_buttons_without_name.append("button")

    def handle_endtag(self, tag):
        if tag == "table":
            self._table = None


def css_classes(css_path: Path):
    content = css_path.read_text(encoding="utf-8")
    return set(re.findall(r"\.([a-zA-Z_][\w-]*)", content))


def validate(html_path: Path, css_path: Path) -> int:
    parser = AuditParser()
    parser.feed(html_path.read_text(encoding="utf-8"))
    allowed = css_classes(css_path)
    errors = []
    warnings = []

    unknown = sorted({c for c in parser.classes if c.startswith("ux-local-") and c not in allowed})
    nonstandard = sorted({c for c in parser.classes if not c.startswith("ux-local-")})
    if unknown:
        errors.append(f"Clases ux-local-* no definidas en CSS: {', '.join(unknown)}")
    if nonstandard:
        errors.append(f"Clases fuera del estándar ux-local-*: {', '.join(nonstandard)}")
    if parser.inline_styles:
        errors.append(f"Estilos inline detectados en: {', '.join(parser.inline_styles)}")
    if parser.external_css:
        errors.append("CSS externo detectado: " + ", ".join(parser.external_css))
    if parser.images_without_alt:
        errors.append("Imágenes sin atributo alt: " + ", ".join(parser.images_without_alt))
    if parser.icon_buttons_without_name:
        errors.append("Botón de icono sin aria-label/title")

    for idx, table in enumerate(parser.tables, 1):
        if not table["caption"]:
            errors.append(f"Tabla {idx}: falta <caption>")
        if not table["ths"]:
            warnings.append(f"Tabla {idx}: no tiene <th>")
        elif any(scope not in {"col", "row", "colgroup", "rowgroup"} for scope in table["ths"]):
            errors.append(f"Tabla {idx}: todos los <th> deben tener scope válido")

    print(f"FILE: {html_path}")
    for item in warnings:
        print(f"WARN: {item}")
    for item in errors:
        print(f"FAIL: {item}")
    if errors:
        print(f"RESULT: FAIL ({len(errors)} errores, {len(warnings)} advertencias)")
        return 1
    print(f"RESULT: PASS ({len(warnings)} advertencias)")
    return 0


def main() -> int:
    root = Path(__file__).resolve().parent.parent
    parser = argparse.ArgumentParser(description="Valida HTML contra el estándar Front-End local.")
    parser.add_argument("--file", required=True, help="Archivo HTML a validar")
    parser.add_argument("--css", default=str(root / "reference-standards" / "styles-standard.css"), help="CSS de referencia")
    args = parser.parse_args()
    html_path = Path(args.file).resolve()
    css_path = Path(args.css).resolve()
    if not html_path.exists() or not css_path.exists():
        print("FAIL: archivo HTML o CSS de referencia inexistente")
        return 2
    return validate(html_path, css_path)


if __name__ == "__main__":
    sys.exit(main())
