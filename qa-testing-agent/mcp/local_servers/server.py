#!/usr/bin/env python3
from mcp_runtime import run
from utils import run_json_script, safe_path, temp_json, PROJECT
import json

STORE=PROJECT/'mcp/data/jira_issues.json'
TOOLS=[
 {"name":"jira_get_issue_local","description":"Lee una incidencia Jira del almacén local de demo.","inputSchema":{"type":"object","properties":{"key":{"type":"string"}},"required":["key"]}},
 {"name":"jira_prepare_ticket","description":"Valida/prepara un ticket DQA Perú sin publicarlo en Jira remoto.","inputSchema":{"type":"object","properties":{"ticket":{"type":"object"}},"required":["ticket"]}},
 {"name":"jira_upsert_issue_local","description":"Crea/actualiza un issue SOLO en el store local. Requiere confirm=true.","inputSchema":{"type":"object","properties":{"key":{"type":"string"},"fields":{"type":"object"},"confirm":{"type":"boolean"}},"required":["key","fields","confirm"]}},
 {"name":"xray_generate_local","description":"Genera especificación Test/Test Execution Xray de demo desde criterios de aceptación.","inputSchema":{"type":"object","properties":{"request":{"type":"object"}},"required":["request"]}},
 {"name":"coverage_review_local","description":"Analiza cobertura JaCoCo/coverage.py/LCOV en un archivo local.","inputSchema":{"type":"object","properties":{"report":{"type":"string"},"format":{"type":"string"},"threshold":{"type":"number"}},"required":["report"]}}
]

def load_store():
    return json.loads(STORE.read_text(encoding='utf-8')) if STORE.exists() else {}

def handler(name,a):
    if name=='jira_get_issue_local':
        s=load_store(); return s.get(a['key'],{"found":False,"key":a['key']})
    if name=='jira_prepare_ticket':
        p=temp_json(a['ticket'])
        try: return run_json_script('.github/skills/qa-ticket-jira/scripts/validate_qa_ticket.py',[p])
        finally: p.unlink(missing_ok=True)
    if name=='jira_upsert_issue_local':
        if a.get('confirm') is not True: raise ValueError('confirm=true requerido para escribir incluso en Jira local de demo')
        s=load_store(); s[a['key']]=a['fields']; STORE.write_text(json.dumps(s,indent=2,ensure_ascii=False),encoding='utf-8'); return {"saved":True,"key":a['key'],"remote":False}
    if name=='xray_generate_local':
        p=temp_json(a['request']); out=safe_path('output_xray_mcp.json')
        try:
            run_json_script('.github/skills/xray-generator/scripts/generate_xray.py',[p,'--out',out])
            return json.loads(out.read_text(encoding='utf-8'))
        finally: p.unlink(missing_ok=True)
    if name=='coverage_review_local':
        args=[safe_path(a['report'])]
        if a.get('format'): args += ['--format',a['format']]
        args += ['--threshold',str(a.get('threshold',80))]
        return run_json_script('.github/skills/coverage-review/scripts/review_coverage.py',args)
    raise ValueError('Tool no permitida')

if __name__=='__main__': run('qa-local','1.0.0',TOOLS,handler)
