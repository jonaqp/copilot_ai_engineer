#!/usr/bin/env python3
import json, subprocess, sys
from pathlib import Path
base=Path(__file__).resolve().parents[1]
server=base/'mcp/local_servers/server.py'
requests=[
 {"jsonrpc":"2.0","id":1,"method":"initialize","params":{"protocolVersion":"2025-06-18","capabilities":{},"clientInfo":{"name":"suite-test","version":"1"}}},
 {"jsonrpc":"2.0","method":"notifications/initialized","params":{}},
 {"jsonrpc":"2.0","id":2,"method":"tools/list","params":{}}
]
payload=''.join(json.dumps(x)+'\n' for x in requests)
cp=subprocess.run([sys.executable,str(server)],cwd=base,input=payload,text=True,capture_output=True,timeout=20)
if cp.returncode:
    print(cp.stderr); raise SystemExit(cp.returncode)
rows=[json.loads(x) for x in cp.stdout.splitlines() if x.strip()]
assert any(r.get('id')==1 and 'result' in r for r in rows), rows
listrow=next(r for r in rows if r.get('id')==2)
tools=listrow['result']['tools']
assert tools, 'No se descubrieron tools'
print(json.dumps({'status':'ok','server':str(server.relative_to(base)),'tool_count':len(tools),'tools':[t['name'] for t in tools]},indent=2,ensure_ascii=False))
