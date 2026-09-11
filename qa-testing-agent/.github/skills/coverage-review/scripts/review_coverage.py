#!/usr/bin/env python3
import argparse, json, re, xml.etree.ElementTree as ET
from pathlib import Path

def jacoco(path):
    root=ET.parse(path).getroot(); c=None
    for x in root.findall('counter'):
        if x.get('type')=='LINE': c=x
    if c is None: raise ValueError('No LINE counter')
    missed=int(c.get('missed',0)); covered=int(c.get('covered',0)); total=missed+covered
    return 100.0*covered/total if total else 100.0, covered, total

def coverage_xml(path):
    root=ET.parse(path).getroot(); rate=float(root.get('line-rate',0)); total=int(root.get('lines-valid',0)); covered=int(root.get('lines-covered',0)); return rate*100,covered,total

def lcov(path):
    text=Path(path).read_text(errors='ignore'); lf=sum(int(x) for x in re.findall(r'^LF:(\d+)',text,re.M)); lh=sum(int(x) for x in re.findall(r'^LH:(\d+)',text,re.M)); return (100.0*lh/lf if lf else 100.0),lh,lf

def main():
    p=argparse.ArgumentParser(); p.add_argument('report'); p.add_argument('--format',choices=['jacoco','coverage','lcov']); p.add_argument('--threshold',type=float,default=80); a=p.parse_args()
    fmt=a.format or ('lcov' if Path(a.report).name.endswith('.info') else 'jacoco')
    try: pct,cov,total={'jacoco':jacoco,'coverage':coverage_xml,'lcov':lcov}[fmt](a.report)
    except Exception:
        if not a.format and fmt=='jacoco': pct,cov,total=coverage_xml(a.report); fmt='coverage'
        else: raise
    print(json.dumps({'format':fmt,'line_coverage_pct':round(pct,2),'covered_lines':cov,'total_lines':total,'threshold_pct':a.threshold,'meets_threshold':pct>=a.threshold,'note':'Cobertura global; no afirmar new-code coverage salvo que el reporte la provea.'},indent=2,ensure_ascii=False))
if __name__=='__main__': main()
