import json
from pathlib import Path
import sys

BASE = Path(__file__).resolve().parent
sys.path.insert(0, str(BASE))

from impact_engine import Component, Dependency, DependencyGraph, ImpactAnalyzer


def build_graph():
    raw = json.loads((BASE / "sample_system" / "architecture.json").read_text())
    return DependencyGraph(
        [Component(**x) for x in raw["components"]],
        [Dependency(**x) for x in raw["dependencies"]],
    )


def test_pricing_service_reaches_direct_and_indirect_dependents():
    items = build_graph().impact_paths("pricing-service")
    depths = {item.component: item.depth for item in items}
    assert depths["checkout-api"] == 1
    assert depths["cart-service"] == 1
    assert depths["storefront-web"] == 2


def test_undocumented_dependency_is_preserved_as_risk_signal():
    items = build_graph().impact_paths("pricing-service")
    cart = next(item for item in items if item.component == "cart-service")
    assert cart.documented is False


def test_order_schema_change_can_be_no_go():
    report = ImpactAnalyzer(build_graph()).analyze("order-db", "schema")
    assert report["risk"]["score"] >= 75
    assert report["decision"] == "NO-GO"


def test_tests_can_mitigate_but_not_erase_risk():
    analyzer = ImpactAnalyzer(build_graph())
    before = analyzer.analyze("pricing-service", "contract")
    after = analyzer.analyze("pricing-service", "contract", tested=["checkout-api", "cart-service", "storefront-web"])
    assert after["risk"]["score"] < before["risk"]["score"]
