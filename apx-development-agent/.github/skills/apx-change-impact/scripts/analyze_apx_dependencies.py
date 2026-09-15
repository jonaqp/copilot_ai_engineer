#!/usr/bin/env python3
import argparse, json, xml.etree.ElementTree as ET
from pathlib import Path

def lname(tag): return tag.split('}')[-1]
def parse_pom(path):
    root=ET.parse(path).getroot(); deps=[]; modules=[]
    for e in root.iter():
        if lname(e.tag)=='dependency':
            vals={lname(c.tag):c.text for c in e}; deps.append({'groupId':vals.get('groupId'),'artifactId':vals.get('artifactId'),'version':vals.get('version')})
        elif lname(e.tag)=='module' and e.text: modules.append(e.text.strip())
    return deps,modules

def main():
    p=argparse.ArgumentParser();p.add_argument('repo');p.add_argument('--out',default='apx_impact.json');a=p.parse_args();repo=Path(a.repo);allp={}
    for pom in repo.rglob('pom.xml'):
        try: deps,mods=parse_pom(pom); allp[str(pom.relative_to(repo))]={'dependencies':deps,'modules':mods}
        except Exception as e: allp[str(pom.relative_to(repo))]={'error':str(e)}
    out={'poms':allp,'note':'Mapa Maven estatico; complementar con dependencias APX/runtime y consumidores via catalogos/MCP aprobados.'};Path(a.out).write_text(json.dumps(out,indent=2,ensure_ascii=False),encoding='utf-8');print(json.dumps(out,indent=2,ensure_ascii=False))
if __name__=='__main__':main()
