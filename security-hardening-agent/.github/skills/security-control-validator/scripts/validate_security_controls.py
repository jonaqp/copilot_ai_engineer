#!/usr/bin/env python3
import argparse, json
from pathlib import Path

def add(f,ok,control,msg):
    if not ok: f.append({'control':control,'severity':'BLOCKER','message':msg})
def main():
    p=argparse.ArgumentParser();p.add_argument('manifest');a=p.parse_args();d=json.loads(Path(a.manifest).read_text());f=[]
    add(f,bool(d.get('prod_nonprod_segregated')),'SRI-03','No se confirma segregacion de previos y produccion')
    add(f,not bool(d.get('production_data_in_nonprod')),'SRI-03','Se declara dato productivo en no productivo sin tratamiento')
    proto=str(d.get('transport_protocol','')).lower(); add(f,proto in {'https','sftp','ssh','tls'},'STR-01','Protocolo de transporte no esta en allowlist cifrada de demo')
    if proto=='https': add(f,float(d.get('tls_version',0))>=1.2,'STR-02','TLS inferior a 1.2')
    add(f,bool(d.get('official_repository')),'SAP-03','No se confirma repositorio corporativo oficial')
    add(f,bool(d.get('pipeline_security_scans')),'SAP-03','No se confirma analisis automatizado de seguridad/calidad')
    print(json.dumps({'passes_demo_baseline':not f,'findings':f,'note':'Validacion de demo; consultar Arquitectura de Seguridad para alcance y excepciones.'},indent=2,ensure_ascii=False))
if __name__=='__main__':main()
