from pathlib import Path
import sys

root = Path(__file__).resolve().parents[1]
template = root / "demo_arch_radar" / "templates" / "index.html"
script = root / "demo_arch_radar" / "static" / "impact-graph.js"
css = root / "demo_arch_radar" / "static" / "styles.css"

checks = {
    "html_graph_container": 'id="impactGraph"' in template.read_text(encoding="utf-8"),
    "graph_payload": 'id="graphData"' in template.read_text(encoding="utf-8"),
    "svg_renderer": "createElementNS(SVG_NS, 'svg')" in script.read_text(encoding="utf-8"),
    "nodes_renderer": "components.forEach(drawNode)" in script.read_text(encoding="utf-8"),
    "edges_renderer": "dependencies.forEach" in script.read_text(encoding="utf-8"),
    "visible_height": "#impactGraph{width:100%;height:560px}" in css.read_text(encoding="utf-8"),
    "no_cdn_dependency": "cdnjs" not in template.read_text(encoding="utf-8"),
}

failed = [name for name, ok in checks.items() if not ok]
for name, ok in checks.items():
    print(("PASS" if ok else "FAIL") + ": " + name)
if failed:
    print("RESULT: FAIL")
    sys.exit(1)
print("RESULT: PASS")
