#!/usr/bin/env python3
import argparse, subprocess, sys, json
from pathlib import Path
p=argparse.ArgumentParser(description='Genera pack QA local: ticket + Xray + coverage + PR readiness')
p.add_argument('--ticket',required=True);p.add_argument('--xray-request',required=True);p.add_argument('--coverage',required=True);p.add_argument('--pr-evidence',required=True);p.add_argument('--threshold',type=float,default=80);p.add_argument('--out-dir',default='output_qa_pack');a=p.parse_args()
base=Path(__file__).resolve().parents[4];out=(base/a.out_dir).resolve();out.mkdir(parents=True,exist_ok=True)
def run(rel,args,name):
 cp=subprocess.run([sys.executable,str(base/rel),*map(str,args)],cwd=base,text=True,capture_output=True,check=True);(out/name).write_text(cp.stdout,encoding='utf-8')
run('.github/skills/qa-ticket-jira/scripts/validate_qa_ticket.py',[base/a.ticket],'ticket_validation.json')
run('.github/skills/xray-generator/scripts/generate_xray.py',[base/a.xray_request,'--out',out/'xray_tests.json'],'xray_console.json')
run('.github/skills/coverage-review/scripts/review_coverage.py',[base/a.coverage,'--threshold',a.threshold],'coverage.json')
run('.github/skills/qa-pr-readiness/scripts/validate_pr_evidence.py',[base/a.pr_evidence],'pr_readiness.json')
print(json.dumps({'status':'pack-generated','dir':str(out),'remote_jira_write':False},indent=2,ensure_ascii=False))
