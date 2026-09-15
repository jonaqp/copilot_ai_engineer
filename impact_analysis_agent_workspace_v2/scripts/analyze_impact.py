#!/usr/bin/env python3
import argparse, json, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEMO = ROOT / "demo_arch_radar"
sys.path.insert(0, str(DEMO))
from loader import load_graph
from impact_engine import ImpactAnalyzer

p = argparse.ArgumentParser(description="Predictive change impact analysis")
p.add_argument("--graph", required=True)
p.add_argument("--component", required=True)
p.add_argument("--change-type", default="behavior", choices=["behavior","performance","config","dependency","contract","schema"])
p.add_argument("--tested", nargs="*", default=[])
args = p.parse_args()
report = ImpactAnalyzer(load_graph(args.graph)).analyze(args.component, args.change_type, args.tested)
print(json.dumps(report, indent=2, ensure_ascii=False))
