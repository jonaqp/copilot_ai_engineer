#!/usr/bin/env python3
"""Regenerate demo_arch_radar/static-demo.html from architecture and optional impact scenario.

No third-party packages are required. The file is always overwritten atomically.
"""
from __future__ import annotations

import argparse
import html
import json
import os
import sys
from pathlib import Path

SKILL_DIR = Path(__file__).resolve().parents[1]
WORKSPACE = SKILL_DIR.parents[2]
DEMO_DIR = WORKSPACE / "demo_arch_radar"
DEFAULT_GRAPH = DEMO_DIR / "sample_system" / "architecture.json"
DEFAULT_TEMPLATE = DEMO_DIR / "templates" / "static-demo.template.html"
DEFAULT_OUTPUT = DEMO_DIR / "static-demo.html"

sys.path.insert(0, str(DEMO_DIR))
from impact_engine import Component, Dependency, DependencyGraph, ImpactAnalyzer  # noqa: E402


def load_graph(path: Path) -> tuple[dict, DependencyGraph]:
    raw = json.loads(path.read_text(encoding="utf-8"))
    components = [Component(**item) for item in raw.get("components", [])]
    dependencies = [Dependency(**item) for item in raw.get("dependencies", [])]
    return raw, DependencyGraph(components, dependencies)


def summary_html(impact: dict | None, component_count: int, dependency_count: int) -> str:
    if not impact:
        return f'''<section class="card summary">
<div class="metric"><span>Componentes</span><strong>{component_count}</strong><small>en el grafo</small></div>
<div class="metric"><span>Dependencias</span><strong>{dependency_count}</strong><small>detectadas</small></div>
<div class="metric"><span>Modo</span><strong class="decision">BASE</strong><small>sin cambio seleccionado</small></div>
</section>'''
    risk = impact["risk"]
    return f'''<section class="card summary">
<div class="metric"><span>Riesgo</span><strong>{risk["score"]}/100</strong><small>{html.escape(risk["level"])}</small></div>
<div class="metric"><span>Alcance</span><strong>{len(impact["impacts"])}</strong><small>componentes</small></div>
<div class="metric"><span>Decision</span><strong class="decision">{html.escape(impact["decision"])}</strong><small>pre-deploy</small></div>
</section>'''


def validation_html(impact: dict | None) -> str:
    if not impact:
        return ""
    validations = impact.get("required_validations", [])
    if not validations:
        return ""
    items = "".join(f"<li>{html.escape(v)}</li>" for v in validations)
    return f'''<section class="card full"><h2>Validaciones Shift-Left</h2><ul>{items}</ul></section>'''


def render(template: str, raw_graph: dict, impact: dict | None) -> str:
    if impact:
        root = impact["root"]
        page_title = f"Impact Radar - {root['name']}"
        intro = "Vista actualizada a partir del ultimo analisis solicitado al agente."
        context = f"Propagacion desde <strong>{html.escape(root['name'])}</strong> por cambio <strong>{html.escape(impact['change_type'])}</strong>."
        status = "Modo ANALISIS: ROOT, L1, L2+, riesgo y validaciones reflejan el escenario actual."
    else:
        page_title = "Impact Radar - Demo Base"
        intro = "Demo base del ecosistema. Aun no hay un cambio seleccionado ni un efecto domino calculado."
        context = "Mapa base de la aplicacion. Ejecuta un prompt de impacto para convertirlo en un radar resaltado."
        status = "Modo BASE: solo topologia real. El primer prompt de impacto regenerara este archivo y resaltara el escenario."

    replacements = {
        "__PAGE_TITLE__": html.escape(page_title),
        "__INTRO_TEXT__": intro,
        "__SUMMARY_SECTION__": summary_html(impact, len(raw_graph.get("components", [])), len(raw_graph.get("dependencies", []))),
        "__GRAPH_CONTEXT__": context,
        "__VALIDATION_SECTION__": validation_html(impact),
        "__DEMO_STATUS__": status,
        "__GRAPH_DATA__": json.dumps(raw_graph, ensure_ascii=False).replace("</", "<\\/"),
        "__IMPACT_DATA__": (json.dumps(impact, ensure_ascii=False) if impact else "null").replace("</", "<\\/"),
    }
    for token, value in replacements.items():
        template = template.replace(token, value)
    return template


def write_atomic(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(content, encoding="utf-8")
    os.replace(tmp, path)


def main() -> int:
    parser = argparse.ArgumentParser(description="Overwrite static-demo.html with base topology or latest impact scenario.")
    parser.add_argument("--graph", type=Path, default=DEFAULT_GRAPH)
    parser.add_argument("--template", type=Path, default=DEFAULT_TEMPLATE)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--component", help="Root component to analyze. Omit to generate BASE demo.")
    parser.add_argument("--change-type", default="behavior", choices=["behavior", "performance", "config", "dependency", "contract", "schema"])
    parser.add_argument("--tested", default="", help="Comma-separated component ids already tested.")
    args = parser.parse_args()

    raw_graph, graph = load_graph(args.graph)
    impact = None
    if args.component:
        if args.component not in graph.components:
            parser.error(f"Unknown component: {args.component}")
        tested = [x.strip() for x in args.tested.split(",") if x.strip()]
        impact = ImpactAnalyzer(graph).analyze(args.component, args.change_type, tested)

    template = args.template.read_text(encoding="utf-8")
    output = render(template, raw_graph, impact)
    write_atomic(args.output, output)
    mode = "ANALYSIS" if impact else "BASE"
    print(f"PASS: regenerated {args.output} mode={mode}")
    if impact:
        print(f"ROOT={impact['root']['id']} risk={impact['risk']['score']} decision={impact['decision']} impacted={len(impact['impacts'])}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
