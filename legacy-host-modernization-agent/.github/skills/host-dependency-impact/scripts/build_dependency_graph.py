#!/usr/bin/env python3
import argparse, json, re
from pathlib import Path

def scan(root):
    graph={}
    for f in Path(root).rglob('*'):
        if f.is_file() and f.suffix.lower() in {'.cbl','.cob','.cobol'}:
            t=f.read_text(errors='ignore')
            m=re.search(r'PROGRAM-ID\.\s+([A-Z0-9_-]+)',t,re.I)
            name=m.group(1).upper() if m else f.stem.upper()
            calls=sorted(set(x.upper() for x in re.findall(r'\bCALL\s+[\"\']?([A-Z0-9_-]+)',t,re.I)))
            copies=sorted(set(x.upper() for x in re.findall(r'^\s*COPY\s+([A-Z0-9_.-]+)',t,re.I|re.M)))
            graph[name]={'file':str(f),'calls':calls,'copies':copies}
    return graph

def main():
    p=argparse.ArgumentParser(); p.add_argument('root'); p.add_argument('--out',default='host_dependencies.json')
    a=p.parse_args(); g=scan(a.root); Path(a.out).write_text(json.dumps(g,indent=2,ensure_ascii=False),encoding='utf-8'); print(json.dumps(g,indent=2,ensure_ascii=False))
if __name__=='__main__': main()
