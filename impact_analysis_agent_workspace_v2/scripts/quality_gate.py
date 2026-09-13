#!/usr/bin/env python3
import argparse, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEMO = ROOT / "demo_arch_radar"
sys.path.insert(0, str(DEMO))
from loader import load_graph
from impact_engine import ImpactAnalyzer

p = argparse.ArgumentParser(description="Shift-left architecture risk gate")
p.add_argument("--graph", required=True)
p.add_argument("--component", required=True)
p.add_argument("--change-type", required=True, choices=["behavior","performance","config","dependency","contract","schema"])
p.add_argument("--tested", nargs="*", default=[])
args = p.parse_args()
report = ImpactAnalyzer(load_graph(args.graph)).analyze(args.component, args.change_type, args.tested)
print(f"Risk: {report['risk']['score']}/100 ({report['risk']['level']})")
print(f"Decision: {report['decision']}")
print("Impacted:", ", ".join(i["component"] for i in report["impacts"]) or "none")
if report["missing_critical_tests"]:
    print("Missing critical test evidence:", ", ".join(report["missing_critical_tests"]))
raise SystemExit(2 if report["decision"] == "NO-GO" else 0)
