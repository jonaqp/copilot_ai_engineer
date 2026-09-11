#!/usr/bin/env python3
import argparse, json, re
from pathlib import Path

def normalize_steps(case):
    steps=[]
    for i,s in enumerate(case.get('steps',[]),1):
        if isinstance(s,str): steps.append({'index':i,'action':s,'data':'','expected':'Definir resultado esperado'})
        else: steps.append({'index':i,'action':s.get('action',''),'data':s.get('data',''),'expected':s.get('expected','')})
    return steps

def main():
    p=argparse.ArgumentParser(); p.add_argument('request_json'); p.add_argument('--out',default='xray_tests.json'); a=p.parse_args(); d=json.loads(Path(a.request_json).read_text())
    tests=[]
    for idx,c in enumerate(d.get('test_cases',[]),1):
        tests.append({'test_key':None,'summary':c.get('summary') or f"{d.get('feature','Feature')} - Caso {idx}",'status':'New','preconditions':c.get('preconditions',[]),'steps':normalize_steps(c),'evidence_required':c.get('evidence_required',['captura/archivo por fuente']),'test_execution':{'key':None,'status':'New','evidence':[]}})
    out={'source_requirement':d.get('jira_key'),'tests':tests,'note':'Artefacto previo a publicacion. Confirmar plantilla Xray DQA vigente y no publicar sin aprobacion.'}
    Path(a.out).write_text(json.dumps(out,indent=2,ensure_ascii=False),encoding='utf-8'); print(json.dumps(out,indent=2,ensure_ascii=False))
if __name__=='__main__': main()
