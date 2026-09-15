#!/usr/bin/env python3
import argparse, subprocess, sys, json
from pathlib import Path
p=argparse.ArgumentParser(description='Compone host-code-analysis + cobol-modernization-assessment + online-to-batch-conversion')
p.add_argument('source'); p.add_argument('--out-dir',default='output_host_assessment'); a=p.parse_args()
base=Path(__file__).resolve().parents[4]; out=(base/a.out_dir).resolve(); out.mkdir(parents=True,exist_ok=True)
inv=out/'inventory.json'; modern=out/'modernization.json'; batch=out/'online_to_batch.json'
def run(script,args,target=None):
    cp=subprocess.run([sys.executable,str(base/script),*map(str,args)],cwd=base,text=True,capture_output=True,check=True)
    if target: target.write_text(cp.stdout,encoding='utf-8')
    return cp.stdout
run('.github/skills/host-code-analysis/scripts/analyze_cobol.py',[base/a.source,'--out',inv])
run('.github/skills/cobol-modernization-assessment/scripts/assess_modernization.py',[inv,'--out',modern])
run('.github/skills/online-to-batch-conversion/scripts/assess_online_to_batch.py',[inv,'--out',batch])
print(json.dumps({'inventory':str(inv),'modernization':str(modern),'online_to_batch':str(batch)},indent=2,ensure_ascii=False))
