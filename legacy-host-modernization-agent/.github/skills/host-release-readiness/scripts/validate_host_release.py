#!/usr/bin/env python3
import argparse, json
from pathlib import Path
REQUIRED=['project','jira_key','packages_ready','rollback_plan','evidence']
def main():
    p=argparse.ArgumentParser(); p.add_argument('manifest'); a=p.parse_args(); d=json.loads(Path(a.manifest).read_text())
    findings=[]
    for k in REQUIRED:
        if k not in d or d[k] in (None,'',[],False): findings.append({'field':k,'severity':'BLOCKER','message':'Falta o no esta confirmado'})
    if d.get('summary') and not ('Host' in d['summary'] and 'Release' in d['summary']): findings.append({'field':'summary','severity':'WARN','message':'Revisar patron [Peru - proyecto] Host - Release'})
    r={'ready':not any(x['severity']=='BLOCKER' for x in findings),'findings':findings,'note':'Baseline de demo DQA Peru; validar procedimiento vigente.'}
    print(json.dumps(r,indent=2,ensure_ascii=False))
if __name__=='__main__': main()
