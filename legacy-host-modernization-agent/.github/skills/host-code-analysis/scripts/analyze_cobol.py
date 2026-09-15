#!/usr/bin/env python3
import argparse, json, re
from pathlib import Path

def analyze(text):
    def uniq(pattern, flags=re.I|re.M):
        return sorted(set(m.group(1).strip().strip("'\"") for m in re.finditer(pattern, text, flags)))
    return {
        'program_id': (uniq(r'^\s*PROGRAM-ID\.\s+([A-Z0-9_-]+)') or [None])[0],
        'calls': uniq(r'\bCALL\s+[\"\']?([A-Z0-9_-]+)'),
        'copies': uniq(r'^\s*COPY\s+([A-Z0-9_.-]+)'),
        'sql_tables': sorted(set(re.findall(r'\b(?:FROM|JOIN|UPDATE|INTO)\s+([A-Z0-9_.]+)', text, re.I))),
        'cics_commands': sorted(set(re.findall(r'EXEC\s+CICS\s+([A-Z-]+)', text, re.I))),
        'file_descriptors': uniq(r'^\s*FD\s+([A-Z0-9_-]+)'),
        'has_commarea': bool(re.search(r'COMMAREA|DFHCOMMAREA', text, re.I)),
    }

def main():
    p=argparse.ArgumentParser(description='Inventario estatico COBOL/Host')
    p.add_argument('source'); p.add_argument('--out')
    a=p.parse_args(); data=analyze(Path(a.source).read_text(errors='ignore'))
    out=json.dumps(data, indent=2, ensure_ascii=False)
    if a.out: Path(a.out).write_text(out, encoding='utf-8')
    print(out)
if __name__=='__main__': main()
