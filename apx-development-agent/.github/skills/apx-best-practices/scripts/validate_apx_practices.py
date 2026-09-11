#!/usr/bin/env python3
import argparse, json
from pathlib import Path

def main():
    p=argparse.ArgumentParser();p.add_argument('manifest_json');a=p.parse_args();d=json.loads(Path(a.manifest_json).read_text());f=[]
    rt=d.get('resource_type')
    allowed={'ud-online','ud-batch','library','dto','shell-script','statics'}
    if rt not in allowed: f.append({'severity':'BLOCKER','field':'resource_type','message':'Tipo no reconocido por baseline de demo'})
    if rt=='ud-batch' and int(d.get('job_count',0))>1: f.append({'severity':'BLOCKER','field':'job_count','message':'Baseline: una UD Batch contiene un unico job'})
    branch=d.get('branch','')
    if branch and not (branch=='develop' or branch.startswith(('feature/','release/','bugfix/','hotfix/'))): f.append({'severity':'WARN','field':'branch','message':'No coincide con ramas baseline APX consultado'})
    if d.get('coverage_pct') is not None and float(d['coverage_pct'])<80: f.append({'severity':'BLOCKER','field':'coverage_pct','message':'Inferior al baseline APX de 80% sobre nuevo codigo; confirmar metrica exacta del Quality Gate'})
    print(json.dumps({'compliant_demo_baseline':not any(x['severity']=='BLOCKER' for x in f),'findings':f,'note':'Baseline resumido; prevalece normativa APX vigente.'},indent=2,ensure_ascii=False))
if __name__=='__main__':main()
