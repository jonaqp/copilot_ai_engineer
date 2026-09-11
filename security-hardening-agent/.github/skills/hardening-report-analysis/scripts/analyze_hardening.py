#!/usr/bin/env python3
import argparse, csv, json
from pathlib import Path
ORDER={'critical':4,'high':3,'medium':2,'low':1,'info':0}
def load(path):
    p=Path(path)
    if p.suffix.lower()=='.json': return json.loads(p.read_text())
    with p.open(newline='',encoding='utf-8-sig') as f: return list(csv.DictReader(f))
def main():
    p=argparse.ArgumentParser();p.add_argument('report');p.add_argument('--out',default='hardening_analysis.json');a=p.parse_args();rows=load(a.report);fails=[]
    for r in rows:
        status=str(r.get('status') or r.get('resultado') or '').lower()
        if status in {'fail','failed','nok','no cumple','non-compliant'}:
            sev=str(r.get('severity') or r.get('severidad') or 'medium').lower(); fails.append({'control':r.get('control') or r.get('id'),'severity':sev,'evidence':r.get('evidence') or r.get('evidencia'),'recommended_action':r.get('remediation') or r.get('remediacion') or 'Validar con owner y norma de hardening vigente'})
    fails.sort(key=lambda x:ORDER.get(x['severity'],2),reverse=True);out={'failed_controls':fails,'failed_count':len(fails),'requires_human_approval':True};Path(a.out).write_text(json.dumps(out,indent=2,ensure_ascii=False),encoding='utf-8');print(json.dumps(out,indent=2,ensure_ascii=False))
if __name__=='__main__':main()
