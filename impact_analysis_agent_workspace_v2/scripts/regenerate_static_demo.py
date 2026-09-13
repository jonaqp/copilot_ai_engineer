#!/usr/bin/env python3
"""Convenience wrapper for graph-visualization-renderer regeneration script."""
from pathlib import Path
import runpy

SCRIPT = Path(__file__).resolve().parents[1] / ".github" / "skills" / "graph-visualization-renderer" / "scripts" / "regenerate_static_demo.py"
runpy.run_path(str(SCRIPT), run_name="__main__")
