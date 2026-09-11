#!/usr/bin/env python3
import argparse, json
from pathlib import Path
CHECKS=['jira_key','pr_url','hu_linked','required_approvals','latest_build_passed','tests_linked']
def main():
    p=argparse.ArgumentParser();p.add_argument('evidence_json');a=p.parse_args();d=json.loads(Path(a.evidence_json).read_text());f=[]
    for k in CHECKS:
        if d.get(k) in (None,'',False,[],{}): f.append({'field':k,'severity':'BLOCKER','message':'Falta evidencia/confirmacion'})
    for k in ['bot_validation','sonar_passed']:
        if d.get(k) is False: f.append({'field':k,'severity':'BLOCKER','message':'Validacion declarada como fallida'})
    print(json.dumps({'ready':not f,'findings':f,'note':'Aplicabilidad de BOT/Sonar depende del desarrollo; confirmar plantilla DQA vigente.'},indent=2,ensure_ascii=False))
if __name__=='__main__':main()
