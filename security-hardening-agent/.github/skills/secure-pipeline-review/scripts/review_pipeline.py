#!/usr/bin/env python3
import argparse, json, re
from pathlib import Path
KEYS={'build':['build','compile','package'],'test':['test','pytest','junit'],'quality':['sonar','quality'],'security':['chimera','sast','security','scan','dependency-check']}
def main():
    p=argparse.ArgumentParser();p.add_argument('pipeline_file');a=p.parse_args();t=Path(a.pipeline_file).read_text(errors='ignore').lower();checks={k:any(x in t for x in vals) for k,vals in KEYS.items()};print(json.dumps({'checks':checks,'missing':[k for k,v in checks.items() if not v],'note':'Deteccion por texto; presencia de stage no prueba ejecucion satisfactoria. Verificar evidencias de pipeline.'},indent=2,ensure_ascii=False))
if __name__=='__main__':main()
