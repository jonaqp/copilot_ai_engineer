#!/usr/bin/env python3
import subprocess
import sys

cmd = [
    sys.executable,
    "-m",
    "pytest",
    "--cov=demo_shop",
    "--cov-branch",
    "--cov-report=term-missing",
    "--cov-report=xml:coverage.xml",
]
raise SystemExit(subprocess.call(cmd))
