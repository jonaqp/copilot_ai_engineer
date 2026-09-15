#!/usr/bin/env python3
from pathlib import Path
import re, json, argparse

def inventory(root: Path):
    out={'programs':[], 'layouts':[], 'jobs':[]}
    for f in sorted((root/'src').glob('*.host')):
        txt=f.read_text(errors='ignore')
        m=re.search(r'^PROGRAM\s+([A-Z0-9-]+)',txt,re.M)
        calls=re.findall(r'CALL\s+([A-Z0-9-]+)',txt)
        out['programs'].append({'file':str(f),'program':m.group(1) if m else f.stem,'calls':calls})
    for f in sorted((root/'layouts').glob('*')):
        out['layouts'].append({'file':str(f),'name':f.name})
    for f in sorted((root/'jcl').glob('*.jcl')):
        txt=f.read_text(errors='ignore')
        pgms=re.findall(r'PGM=([A-Z0-9-]+)',txt)
        out['jobs'].append({'file':str(f),'programs':pgms})
    return out

if __name__=='__main__':
    p=argparse.ArgumentParser()
    p.add_argument('root',nargs='?',default='demo_host_migration/legacy_host')
    p.add_argument('--out')
    a=p.parse_args()
    data=inventory(Path(a.root)); text=json.dumps(data,indent=2)
    if a.out:
        out=Path(a.out); out.parent.mkdir(parents=True,exist_ok=True); out.write_text(text)
    print(text)
