#!/usr/bin/env python3
import subprocess, sys, tempfile
from pathlib import Path
base = Path(__file__).resolve().parents[1]
with tempfile.TemporaryDirectory(prefix='bbva_security_demo_') as td:
    subprocess.run([
        sys.executable,
        str(base/'.github/skills/security-remediation-plan/scripts/run_security_hardening_pack.py'),
        '--report', 'examples/hardening_report.csv',
        '--manifest', 'examples/security_manifest.json',
        '--pipeline', 'examples/Jenkinsfile',
        '--out-dir', td
    ], cwd=base, check=True)
print('Security demo OK: hardening + controles + pipeline + remediacion ejecutados.')
