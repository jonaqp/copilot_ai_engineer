from pathlib import Path
import subprocess, sys, json, tempfile

PROJECT = Path(__file__).resolve().parents[2]

def safe_path(value):
    p=(PROJECT/str(value)).resolve() if not Path(str(value)).is_absolute() else Path(str(value)).resolve()
    try:
        p.relative_to(PROJECT)
    except ValueError:
        raise ValueError("La ruta debe estar dentro del proyecto de demo")
    return p

def run_json_script(rel_script, args):
    script=safe_path(rel_script)
    cp=subprocess.run([sys.executable,str(script),*map(str,args)],cwd=PROJECT,text=True,capture_output=True,timeout=60)
    if cp.returncode != 0:
        raise RuntimeError(cp.stderr or cp.stdout or f"script rc={cp.returncode}")
    txt=cp.stdout.strip()
    try:
        return json.loads(txt)
    except Exception:
        return {"stdout":txt}

def temp_json(data):
    fd=tempfile.NamedTemporaryFile(mode='w',suffix='.json',delete=False,encoding='utf-8',dir=PROJECT)
    json.dump(data,fd,ensure_ascii=False,indent=2); fd.close()
    return Path(fd.name)
