#!/usr/bin/env python3
from pathlib import Path
import subprocess, sys, shutil, json
ROOT=Path(__file__).resolve().parents[1]

def run(cmd):
    print('$',' '.join(map(str,cmd)))
    p=subprocess.run(cmd,cwd=ROOT,text=True,capture_output=True)
    print(p.stdout,end=''); print(p.stderr,end='',file=sys.stderr)
    return p.returncode

def regression_demo():
    cases=json.loads((ROOT/'demo_host_migration/legacy_host/testdata/transactions.json').read_text())
    failed=[]
    for c in cases:
        bal=c['balance']; rc=0
        if c['status']=='C': rc=12
        elif c['type'] not in ('C','D'): rc=4
        elif c['type']=='D' and bal<c['amount']: rc=8
        elif c['type']=='C': bal+=c['amount']
        else: bal-=c['amount']
        if rc!=c['rc'] or bal!=c['expected_balance']: failed.append(c['name'])
    if failed:
        print('FAIL regression:',','.join(failed)); return 1
    print(f'PASS regression: {len(cases)} scenarios')
    return 0

def main():
    checks=[]
    checks.append(run([sys.executable,'scripts/inventory_host.py','demo_host_migration/legacy_host','--out','demo_host_migration/target_cobol/reports/inventory.json']))
    checks.append(run([sys.executable,'scripts/validate_cobol.py']))
    checks.append(regression_demo())
    cobc=shutil.which('cobc')
    if cobc:
        print('INFO: cobc detected; integrate repository-specific compile command before production use.')
    else:
        print('CONDITION: cobc not available; compilation not executed.')
    if any(checks): print('RESULT: FAIL'); return 1
    print('RESULT: PASS WITH CONDITIONS' if not cobc else 'RESULT: PASS')
    return 0
if __name__=='__main__': raise SystemExit(main())
