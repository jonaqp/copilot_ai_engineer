#!/usr/bin/env python3
import argparse, json
from pathlib import Path

def main():
    p=argparse.ArgumentParser();p.add_argument('repo');p.add_argument('--branch');a=p.parse_args();r=Path(a.repo);f=[]
    for item in ['pom.xml']:
        if not (r/item).exists(): f.append({'severity':'WARN','check':item,'message':'No se encontro; confirmar tipo de recurso APX'})
    if not ((r/'apx.json').exists() or (r/'Jenkinsfile').exists()): f.append({'severity':'INFO','check':'pipeline-metadata','message':'No se encontro apx.json/Jenkinsfile en raiz; validar estructura vigente'})
    if a.branch and a.branch.lower()=='master': f.append({'severity':'WARN','check':'branch','message':'Baseline APX consultado usa develop como origen; validar modelo vigente'})
    tests=list(r.rglob('*Test.java'))+list(r.rglob('*Tests.java'))
    if not tests: f.append({'severity':'WARN','check':'tests','message':'No se detectaron tests Java por convencion simple'})
    print(json.dumps({'repo':str(r),'findings':f,'test_files_detected':len(tests),'note':'Revision estatica parcial; complementar con pipeline, Sonar y Chimera.'},indent=2,ensure_ascii=False))
if __name__=='__main__':main()
