#!/usr/bin/env python3
from pathlib import Path
import argparse, re
REQ=['IDENTIFICATION DIVISION.','PROGRAM-ID.','DATA DIVISION.','PROCEDURE DIVISION']

def validate_file(path):
    txt=path.read_text(errors='ignore')
    errors=[]; warnings=[]
    for r in REQ:
        if r not in txt: errors.append(f'missing: {r}')
    if re.search(r'\bGOTO\b|\bGO TO\b',txt,re.I): errors.append('new GO TO/GOTO detected')
    if re.search(r'\bTODO\b|\bFIXME\b|<PLACEHOLDER>',txt,re.I): errors.append('placeholder detected')
    if len(txt.splitlines())>400: warnings.append('large program; review paragraph responsibilities')
    return errors,warnings

def main():
    p=argparse.ArgumentParser(); p.add_argument('root',nargs='?',default='demo_host_migration/target_cobol/src'); a=p.parse_args()
    files=list(Path(a.root).glob('*.cbl'))
    if not files: print('FAIL: no COBOL programs found'); return 2
    bad=0
    for f in files:
        e,w=validate_file(f); print(f'[{"PASS" if not e else "FAIL"}] {f.name}')
        for x in e: print('  ERROR:',x)
        for x in w: print('  WARN:',x)
        bad += bool(e)
    return 1 if bad else 0
if __name__=='__main__': raise SystemExit(main())
