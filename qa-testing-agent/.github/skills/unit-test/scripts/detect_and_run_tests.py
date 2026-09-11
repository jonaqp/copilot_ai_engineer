#!/usr/bin/env python3
import argparse, json, subprocess
from pathlib import Path
DETECT=[('pytest',['pytest','-q']),('pom.xml',['mvn','test']),('build.gradle',['gradle','test']),('package.json',['npm','test','--','--runInBand'])]
def detect(root):
    root=Path(root)
    if (root/'pytest.ini').exists() or (root/'pyproject.toml').exists() or any(root.glob('test*.py')) or (root/'tests').exists(): return ['pytest','-q']
    for marker,cmd in DETECT[1:]:
        if (root/marker).exists(): return cmd
    return None

def main():
    p=argparse.ArgumentParser(description='Detecta y opcionalmente ejecuta tests conocidos')
    p.add_argument('root'); p.add_argument('--run',action='store_true'); p.add_argument('--timeout',type=int,default=120)
    a=p.parse_args(); cmd=detect(a.root); result={'detected_command':cmd,'executed':False}
    if a.run and cmd:
        cp=subprocess.run(cmd,cwd=a.root,text=True,capture_output=True,timeout=a.timeout,shell=False)
        result.update(executed=True,returncode=cp.returncode,stdout=cp.stdout[-5000:],stderr=cp.stderr[-5000:])
    print(json.dumps(result,indent=2,ensure_ascii=False))
if __name__=='__main__': main()
