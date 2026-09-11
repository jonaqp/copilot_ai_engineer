#!/usr/bin/env python3
import argparse, json, re
from pathlib import Path
FIB={1,2,3,5,8,13,21,34,55,89}
REQ=['summary','status','issue_type','labels','team_backlog','feature_link','item_type','tech_stack','dor','dod','acceptance_criteria','story_points','description','test_link']
def main():
    p=argparse.ArgumentParser(); p.add_argument('ticket_json'); a=p.parse_args(); d=json.loads(Path(a.ticket_json).read_text()); f=[]
    for k in REQ:
        if d.get(k) in (None,'',[],{}): f.append({'field':k,'severity':'BLOCKER','message':'Campo requerido por baseline DQA demo'})
    if d.get('status')!='Ready': f.append({'field':'status','severity':'WARN','message':'Baseline de primer envio DQA: Ready'})
    if d.get('item_type') and str(d['item_type']).lower()!='technical': f.append({'field':'item_type','severity':'WARN','message':'Baseline observado: Technical'})
    if isinstance(d.get('story_points'),(int,float)) and d['story_points'] not in FIB: f.append({'field':'story_points','severity':'WARN','message':'Usar escala Fibonacci segun baseline'})
    if d.get('summary') and not d['summary'].startswith('[Peru -'): f.append({'field':'summary','severity':'WARN','message':'Patron esperado: [Peru - proyecto] [Proceso] [Detalle]'})
    print(json.dumps({'valid':not any(x['severity']=='BLOCKER' for x in f),'findings':f,'ticket':d},indent=2,ensure_ascii=False))
if __name__=='__main__': main()
