#!/usr/bin/env python3
import argparse, subprocess, sys, json
from pathlib import Path
p=argparse.ArgumentParser(description='Compone análisis hardening + controles + pipeline + plan de remediación')
p.add_argument('--report',required=True);p.add_argument('--manifest',required=True);p.add_argument('--pipeline',required=True);p.add_argument('--out-dir',default='output_security_pack');a=p.parse_args()
base=Path(__file__).resolve().parents[4];out=(base/a.out_dir).resolve();out.mkdir(parents=True,exist_ok=True)
def run(rel,args,name):
 cp=subprocess.run([sys.executable,str(base/rel),*map(str,args)],cwd=base,text=True,capture_output=True,check=True);(out/name).write_text(cp.stdout,encoding='utf-8');return cp.stdout
analysis=out/'hardening.json'
subprocess.run([sys.executable,str(base/'.github/skills/hardening-report-analysis/scripts/analyze_hardening.py'),str(base/a.report),'--out',str(analysis)],cwd=base,check=True,capture_output=True,text=True)
run('.github/skills/security-control-validator/scripts/validate_security_controls.py',[base/a.manifest],'controls.json')
run('.github/skills/secure-pipeline-review/scripts/review_pipeline.py',[base/a.pipeline],'pipeline.json')
subprocess.run([sys.executable,str(base/'.github/skills/security-remediation-plan/scripts/build_remediation_plan.py'),str(analysis),'--out',str(out/'remediation.json')],cwd=base,check=True,capture_output=True,text=True)
print(json.dumps({'status':'pack-generated','dir':str(out),'automatic_remediation':False},indent=2,ensure_ascii=False))
