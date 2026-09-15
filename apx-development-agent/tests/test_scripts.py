import subprocess,sys
from pathlib import Path

def test_demo_flow():
    base=Path(__file__).resolve().parents[1]
    cp=subprocess.run([sys.executable,str(base/'scripts/run_demo_flow.py')],cwd=base,capture_output=True,text=True)
    assert cp.returncode==0, cp.stderr
