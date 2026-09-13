#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import json
import re
import sys

root = Path(__file__).resolve().parents[1]
html_path = Path(sys.argv[1]) if len(sys.argv) > 1 else root / "demo_arch_radar" / "static-demo.html"
if not html_path.is_absolute():
    html_path = root / html_path
script = root / "demo_arch_radar" / "static" / "impact-graph.js"
css = root / "demo_arch_radar" / "static" / "styles.css"

html_text = html_path.read_text(encoding="utf-8")
js_text = script.read_text(encoding="utf-8")
css_text = css.read_text(encoding="utf-8")

def embedded_json(element_id: str):
    pattern = rf'<script id="{re.escape(element_id)}" type="application/json">(.*?)</script>'
    match = re.search(pattern, html_text, re.S)
    if not match:
        raise ValueError(f"missing {element_id}")
    value = match.group(1).strip().replace("<\\/", "</")
    return json.loads(value)

try:
    graph = embedded_json("graphData")
    impact = embedded_json("impactData")
    payload_ok = bool(graph.get("components")) and isinstance(graph.get("dependencies"), list)
except Exception:
    graph, impact, payload_ok = {}, None, False

checks = {
    "html_graph_container": 'id="impactGraph"' in html_text,
    "graph_payload": payload_ok,
    "svg_renderer": "createElementNS(SVG_NS, 'svg')" in js_text,
    "nodes_renderer": "components.forEach(drawNode)" in js_text,
    "edges_renderer": "dependencies.forEach" in js_text,
    "visible_height": "#impactGraph{width:100%;height:560px}" in css_text,
    "no_cdn_dependency": all(token not in html_text.lower() for token in ["cdnjs", "unpkg.com", "jsdelivr.net"]),
    "regenerable_marker": "Archivo regenerable" in html_text,
}

mode = "ANALYSIS" if impact else "BASE"
if impact:
    root_id = impact.get("root", {}).get("id")
    checks["analysis_root_present"] = bool(root_id) and root_id in html_text
    checks["analysis_risk_present"] = str(impact.get("risk", {}).get("score", "")) in html_text
    checks["analysis_decision_present"] = str(impact.get("decision", "")) in html_text
else:
    checks["base_has_no_impact"] = 'id="impactData" type="application/json">null</script>' in html_text
    checks["base_mode_label"] = "Modo BASE" in html_text

failed = [name for name, ok in checks.items() if not ok]
for name, ok in checks.items():
    print(("PASS" if ok else "FAIL") + ": " + name)
print(f"MODE: {mode}")
print(f"FILE: {html_path}")
if failed:
    print("RESULT: FAIL")
    sys.exit(1)
print("RESULT: PASS")
