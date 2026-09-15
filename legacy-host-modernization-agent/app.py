from flask import Flask, jsonify, render_template
from agent_config import CONFIG
import json, subprocess, sys
from pathlib import Path
import os

app = Flask(__name__)
BASE = Path(__file__).resolve().parent

@app.get('/')
def index():
    return render_template('index.html', config=CONFIG)

@app.get('/api/health')
def health():
    return jsonify({'status':'ok','agent':CONFIG['title'],'model_recommended':CONFIG['model']})

@app.get('/api/config')
def config():
    return jsonify(CONFIG)

@app.post('/api/demo/<flow>')
def demo(flow):
    spec = CONFIG.get('demo_commands', {}).get(flow)
    if not spec:
        return jsonify({'error':'Flujo no permitido','allowed':list(CONFIG.get('demo_commands',{}))}), 404
    cp = subprocess.run([sys.executable, *spec], cwd=BASE, text=True, capture_output=True, timeout=30)
    return jsonify({'flow':flow,'returncode':cp.returncode,'stdout':cp.stdout,'stderr':cp.stderr}), (200 if cp.returncode==0 else 400)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=os.getenv('FLASK_DEBUG') == '1')
