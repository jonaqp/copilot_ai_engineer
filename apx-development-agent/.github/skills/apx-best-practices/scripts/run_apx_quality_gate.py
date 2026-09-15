#!/usr/bin/env python3
import argparse, subprocess, sys, json
from pathlib import Path
p=argparse.ArgumentParser(description='Compone revisión APX + best practices + coverage + dependencias')
p.add_argument('--repo',required=True);p.add_argument('--manifest',required=True);p.add_argument('--coverage',required=True);p.add_argument('--branch',required=True);p.add_argument('--threshold',type=float,default=80);p.add_argument('--out-dir',default='output_apx_gate');a=p.parse_args()
base=Path(__file__).resolve().parents[4];out=(base/a.out_dir).resolve();out.mkdir(parents=True,exist_ok=True)
def run(rel,args,name):
 cp=subprocess.run([sys.executable,str(base/rel),*map(str,args)],cwd=base,text=True,capture_output=True,check=True);(out/name).write_text(cp.stdout,encoding='utf-8')
run('.github/skills/apx-code-review/scripts/review_apx_repo.py',[base/a.repo,'--branch',a.branch],'repo_review.json')
run('.github/skills/apx-best-practices/scripts/validate_apx_practices.py',[base/a.manifest],'best_practices.json')
run('.github/skills/apx-testing/scripts/review_apx_coverage.py',[base/a.coverage,'--threshold',a.threshold],'coverage.json')
run('.github/skills/apx-change-impact/scripts/analyze_apx_dependencies.py',[base/a.repo,'--out',out/'dependencies.json'],'dependencies_console.json')
print(json.dumps({'status':'gate-generated','dir':str(out),'note':'La evidencia del Quality Gate oficial prevalece sobre este análisis local.'},indent=2,ensure_ascii=False))
