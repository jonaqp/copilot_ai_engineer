#!/usr/bin/env python3
import subprocess, sys, tempfile
from pathlib import Path
base = Path(__file__).resolve().parents[1]
with tempfile.TemporaryDirectory(prefix='bbva_host_demo_') as td:
    subprocess.run([
        sys.executable,
        str(base/'.github/skills/cobol-modernization-assessment/scripts/run_host_assessment.py'),
        'examples/sample_online.cbl', '--out-dir', td
    ], cwd=base, check=True)
    subprocess.run([
        sys.executable,
        str(base/'.github/skills/host-release-readiness/scripts/validate_host_release.py'),
        str(base/'examples/host_release.json')
    ], cwd=base, check=True)
print('Legacy/Host demo OK: composicion de Skills + readiness ejecutados.')
