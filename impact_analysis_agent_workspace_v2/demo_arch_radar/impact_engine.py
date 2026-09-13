from __future__ import annotations

from dataclasses import dataclass, asdict
from collections import defaultdict, deque
from typing import Dict, Iterable, List, Tuple


@dataclass(frozen=True)
class Component:
    id: str
    name: str
    kind: str
    criticality: int
    owner: str


@dataclass(frozen=True)
class Dependency:
    source: str
    target: str
    kind: str
    documented: bool = True


@dataclass(frozen=True)
class ImpactItem:
    component: str
    depth: int
    path: List[str]
    dependency_kind: str
    documented: bool
    criticality: int
    validation: str


class DependencyGraph:
    def __init__(self, components: Iterable[Component], dependencies: Iterable[Dependency]):
        self.components: Dict[str, Component] = {c.id: c for c in components}
        self.dependencies = list(dependencies)
        self._reverse: Dict[str, List[Dependency]] = defaultdict(list)
        for dep in self.dependencies:
            if dep.source not in self.components or dep.target not in self.components:
                raise ValueError(f"Unknown component in dependency: {dep}")
            self._reverse[dep.target].append(dep)

    def dependents_of(self, target: str) -> List[Dependency]:
        return list(self._reverse.get(target, []))

    def impact_paths(self, target: str, max_depth: int = 6) -> List[ImpactItem]:
        if target not in self.components:
            raise KeyError(f"Unknown component: {target}")

        results: List[ImpactItem] = []
        queue = deque([(target, [target], 0)])
        best_depth = {target: 0}

        while queue:
            current, path, depth = queue.popleft()
            if depth >= max_depth:
                continue
            for dep in self.dependents_of(current):
                child = dep.source
                next_depth = depth + 1
                if child in best_depth and best_depth[child] <= next_depth:
                    continue
                best_depth[child] = next_depth
                next_path = [child] + path
                component = self.components[child]
                results.append(
                    ImpactItem(
                        component=child,
                        depth=next_depth,
                        path=next_path,
                        dependency_kind=dep.kind,
                        documented=dep.documented,
                        criticality=component.criticality,
                        validation=self._validation_for(dep.kind, next_depth),
                    )
                )
                queue.append((child, next_path, next_depth))
        return sorted(results, key=lambda x: (x.depth, -x.criticality, x.component))

    @staticmethod
    def _validation_for(kind: str, depth: int) -> str:
        mapping = {
            "sync-api": "contract + integration test",
            "async-event": "event contract + consumer regression",
            "database": "schema compatibility + integration test",
            "library": "unit + regression test",
            "config": "configuration smoke test",
            "ui-contract": "frontend contract + functional test",
        }
        base = mapping.get(kind, "targeted regression test")
        if depth >= 2:
            return base + " + transitive regression"
        return base


class RiskScorer:
    BASE = {
        "behavior": 15,
        "performance": 20,
        "config": 25,
        "dependency": 30,
        "contract": 40,
        "schema": 45,
    }

    def score(self, root: Component, impacts: List[ImpactItem], change_type: str, tested: Iterable[str] = ()) -> Tuple[int, str, List[str]]:
        tested_set = set(tested)
        score = self.BASE.get(change_type, 20)
        factors: List[str] = [f"base:{change_type}={score}"]

        criticality_weight = max(0, min(root.criticality, 5) - 1) * 5
        score += criticality_weight
        factors.append(f"root_criticality:+{criticality_weight}")

        reach_weight = min(len(impacts) * 4, 20)
        score += reach_weight
        factors.append(f"reachable_components:+{reach_weight}")

        max_depth = max((i.depth for i in impacts), default=0)
        depth_weight = min(max_depth * 4, 12)
        score += depth_weight
        factors.append(f"propagation_depth:+{depth_weight}")

        hidden = sum(1 for i in impacts if not i.documented)
        hidden_weight = min(hidden * 6, 18)
        score += hidden_weight
        factors.append(f"undocumented_edges:+{hidden_weight}")

        critical_impacts = [i for i in impacts if i.criticality >= 4]
        covered_critical = sum(1 for i in critical_impacts if i.component in tested_set)
        mitigation = min(covered_critical * 5, 15)
        if mitigation:
            score -= mitigation
            factors.append(f"critical_tests:-{mitigation}")

        score = max(0, min(score, 100))
        level = "Bajo" if score < 25 else "Medio" if score < 50 else "Alto" if score < 75 else "Crítico"
        return score, level, factors


class ImpactAnalyzer:
    def __init__(self, graph: DependencyGraph):
        self.graph = graph
        self.scorer = RiskScorer()

    def analyze(self, component_id: str, change_type: str, tested: Iterable[str] = ()) -> dict:
        root = self.graph.components[component_id]
        impacts = self.graph.impact_paths(component_id)
        score, level, factors = self.scorer.score(root, impacts, change_type, tested)
        tested_set = set(tested)
        missing = [i.component for i in impacts if i.criticality >= 4 and i.component not in tested_set]

        if level == "Crítico" and missing:
            decision = "NO-GO"
        elif level in {"Alto", "Crítico"} or missing:
            decision = "GO WITH CONDITIONS"
        else:
            decision = "GO"

        return {
            "root": asdict(root),
            "change_type": change_type,
            "impacts": [asdict(i) for i in impacts],
            "risk": {"score": score, "level": level, "factors": factors},
            "required_validations": sorted({i.validation for i in impacts}),
            "missing_critical_tests": missing,
            "decision": decision,
        }
