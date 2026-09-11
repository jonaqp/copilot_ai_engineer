#!/usr/bin/env python3
import subprocess, sys, tempfile
from pathlib import Path
base = Path(__file__).resolve().parents[1]
with tempfile.TemporaryDirectory(prefix='bbva_apx_demo_') as td:
    subprocess.run([
        sys.executable,
        str(base/'.github/skills/apx-best-practices/scripts/run_apx_quality_gate.py'),
        '--repo', 'examples/apx-demo-repo',
        '--manifest', 'examples/apx_manifest.json',
        '--coverage', 'examples/jacoco.xml',
        '--branch', 'feature/PEDEMO-123',
        '--threshold', '80',
        '--out-dir', td
    ], cwd=base, check=True)
    rendered = Path(td)/'rendered'
    subprocess.run([
        sys.executable,
        str(base/'.github/skills/apx-code-generation/scripts/render_from_approved_template.py'),
        '--template-dir', 'examples/apx-template-approved',
        '--params', 'examples/apx_template_params.json',
        '--output-dir', str(rendered)
    ], cwd=base, check=True)
print('APX demo OK: quality gate compuesto + render desde plantilla aprobada ejecutados.')
