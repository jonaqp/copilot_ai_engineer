from pathlib import Path
from flask import Flask, render_template, request
from loader import load_graph
from impact_engine import ImpactAnalyzer

BASE = Path(__file__).resolve().parent
GRAPH_PATH = BASE / "sample_system" / "architecture.json"

app = Flask(__name__)
graph = load_graph(GRAPH_PATH)
analyzer = ImpactAnalyzer(graph)


@app.route("/", methods=["GET", "POST"])
def index():
    selected = request.form.get("component", "pricing-service")
    change_type = request.form.get("change_type", "contract")
    tested = request.form.getlist("tested")
    report = analyzer.analyze(selected, change_type, tested) if request.method == "POST" else None
    components = sorted(graph.components.values(), key=lambda c: c.name)
    return render_template(
        "index.html",
        components=components,
        selected=selected,
        change_type=change_type,
        report=report,
    )


if __name__ == "__main__":
    app.run(debug=True)
