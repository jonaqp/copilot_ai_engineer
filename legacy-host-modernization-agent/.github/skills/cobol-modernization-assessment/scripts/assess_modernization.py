#!/usr/bin/env python3
import argparse, json
from pathlib import Path

def score(inv):
    points=0; reasons=[]
    for key, weight, label in [('cics_commands',3,'acoplamiento CICS'),('calls',1,'llamadas a otros programas'),('copies',1,'copybooks'),('sql_tables',2,'acceso SQL'),('file_descriptors',2,'archivos')]:
        n=len(inv.get(key,[])); points += min(n,4)*weight
        if n: reasons.append(f'{label}: {n}')
    if inv.get('has_commarea'): points+=4; reasons.append('uso de COMMAREA')
    level='alto' if points>=12 else 'medio' if points>=6 else 'bajo'
    return {'risk_score':points,'risk_level':level,'reasons':reasons,
            'recommendation':'Priorizar desacople incremental, caracterizacion y pruebas de regresion; no reescribir directamente sin mapa de dependencias.'}

def main():
    p=argparse.ArgumentParser(); p.add_argument('inventory_json'); p.add_argument('--out')
    a=p.parse_args(); data=score(json.loads(Path(a.inventory_json).read_text()))
    s=json.dumps(data,indent=2,ensure_ascii=False); print(s)
    if a.out: Path(a.out).write_text(s,encoding='utf-8')
if __name__=='__main__': main()
