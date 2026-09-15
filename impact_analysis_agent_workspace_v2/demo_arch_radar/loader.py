import json
from pathlib import Path
from impact_engine import Component, Dependency, DependencyGraph


def load_graph(path: str | Path) -> DependencyGraph:
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    components = [Component(**item) for item in data["components"]]
    dependencies = [Dependency(**item) for item in data["dependencies"]]
    return DependencyGraph(components, dependencies)
