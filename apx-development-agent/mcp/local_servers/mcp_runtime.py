#!/usr/bin/env python3
"""Runtime MCP stdio minimo para demos locales.

Implementa initialize, ping, tools/list y tools/call con JSON-RPC por stdin/stdout.
No abre puertos ni necesita librerias externas.
"""
import json, sys, traceback

PROTOCOL_VERSION = "2025-06-18"

def _send(payload):
    sys.stdout.write(json.dumps(payload, ensure_ascii=False) + "\n")
    sys.stdout.flush()

def _ok(req_id, result):
    _send({"jsonrpc":"2.0","id":req_id,"result":result})

def _err(req_id, code, message, data=None):
    obj={"code":code,"message":message}
    if data is not None: obj["data"]=data
    _send({"jsonrpc":"2.0","id":req_id,"error":obj})

def run(server_name, server_version, tools, handler):
    for raw in sys.stdin:
        raw=raw.strip()
        if not raw:
            continue
        try:
            req=json.loads(raw)
            method=req.get("method")
            req_id=req.get("id")
            if method == "notifications/initialized":
                continue
            if method == "initialize":
                requested=(req.get("params") or {}).get("protocolVersion")
                _ok(req_id, {
                    "protocolVersion": requested or PROTOCOL_VERSION,
                    "capabilities": {"tools": {"listChanged": False}},
                    "serverInfo": {"name": server_name, "version": server_version}
                })
            elif method == "ping":
                _ok(req_id,{})
            elif method == "tools/list":
                _ok(req_id,{"tools":tools})
            elif method == "tools/call":
                p=req.get("params") or {}
                name=p.get("name")
                args=p.get("arguments") or {}
                try:
                    result=handler(name,args)
                    if not isinstance(result,str):
                        result=json.dumps(result,indent=2,ensure_ascii=False)
                    _ok(req_id,{"content":[{"type":"text","text":result}],"isError":False})
                except Exception as exc:
                    _ok(req_id,{"content":[{"type":"text","text":f"ERROR: {exc}"}],"isError":True})
            elif method in {"resources/list","prompts/list"}:
                key="resources" if method.startswith("resources") else "prompts"
                _ok(req_id,{key:[]})
            else:
                if req_id is not None:
                    _err(req_id,-32601,"Method not found")
        except Exception as exc:
            _err(None,-32603,"Internal error",str(exc))
