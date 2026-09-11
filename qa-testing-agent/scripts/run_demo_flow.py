#!/usr/bin/env python3
import subprocess, sys, tempfile
from pathlib import Path
base = Path(__file__).resolve().parents[1]
with tempfile.TemporaryDirectory(prefix='bbva_qa_demo_') as td:
    subprocess.run([
        sys.executable,
        str(base/'.github/skills/qa-pr-readiness/scripts/run_qa_certification_pack.py'),
        '--ticket', 'examples/qa_ticket.json',
        '--xray-request', 'examples/qa_request.json',
        '--coverage', 'examples/jacoco.xml',
        '--pr-evidence', 'examples/pr_evidence.json',
        '--threshold', '80',
        '--out-dir', td
    ], cwd=base, check=True)
print('QA demo OK: ticket + Xray + coverage + PR readiness ejecutados.')
