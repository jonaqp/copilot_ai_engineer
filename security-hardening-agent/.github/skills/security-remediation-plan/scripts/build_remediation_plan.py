#!/usr/bin/env python3
import argparse, json
from pathlib import Path
ORDER={'critical':0,'high':1,'medium':2,'low':3,'info':4}
def main():
    p=argparse.ArgumentParser();p.add_argument('findings_json');p.add_argument('--out',default='remediation_plan.json');a=p.parse_args();d=json.loads(Path(a.findings_json).read_text());items=d.get('failed_controls') or d.get('findings') or [];plan=[]
    for i,x in enumerate(sorted(items,key=lambda z:ORDER.get(str(z.get('severity','medium')).lower(),2)),1): plan.append({'priority':i,'control':x.get('control') or x.get('field'),'severity':x.get('severity'),'action':x.get('recommended_action') or x.get('message'),'owner':'POR_ASIGNAR','validation':'Definir evidencia de cierre con owner del control','rollback':'Definir antes de ejecutar cambios','status':'Proposed'})
    out={'plan':plan,'automatic_execution':False};Path(a.out).write_text(json.dumps(out,indent=2,ensure_ascii=False),encoding='utf-8');print(json.dumps(out,indent=2,ensure_ascii=False))
if __name__=='__main__':main()
