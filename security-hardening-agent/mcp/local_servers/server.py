#!/usr/bin/env python3
from mcp_runtime import run
from utils import run_json_script, safe_path
import json
TOOLS=[
 {"name":"analyze_hardening","description":"Analiza reportes CSV/JSON de hardening y prioriza controles fallidos.","inputSchema":{"type":"object","properties":{"report":{"type":"string"}},"required":["report"]}},
 {"name":"validate_security_controls","description":"Valida un manifiesto técnico contra el baseline BBVA Perú de demo.","inputSchema":{"type":"object","properties":{"manifest":{"type":"string"}},"required":["manifest"]}},
 {"name":"review_security_pipeline","description":"Revisa presencia declarativa de build/tests/quality/security en pipeline local; no prueba que hayan pasado.","inputSchema":{"type":"object","properties":{"pipeline":{"type":"string"}},"required":["pipeline"]}},
 {"name":"build_remediation_plan","description":"Genera plan propuesto desde findings; nunca ejecuta remediación sobre infraestructura.","inputSchema":{"type":"object","properties":{"findings":{"type":"string"}},"required":["findings"]}}
]
def handler(name,a):
    if name=='analyze_hardening':
        out=safe_path('output_hardening_mcp.json'); run_json_script('.github/skills/hardening-report-analysis/scripts/analyze_hardening.py',[safe_path(a['report']),'--out',out]); return json.loads(out.read_text(encoding='utf-8'))
    if name=='validate_security_controls': return run_json_script('.github/skills/security-control-validator/scripts/validate_security_controls.py',[safe_path(a['manifest'])])
    if name=='review_security_pipeline': return run_json_script('.github/skills/secure-pipeline-review/scripts/review_pipeline.py',[safe_path(a['pipeline'])])
    if name=='build_remediation_plan':
        out=safe_path('output_remediation_mcp.json'); run_json_script('.github/skills/security-remediation-plan/scripts/build_remediation_plan.py',[safe_path(a['findings']),'--out',out]); return json.loads(out.read_text(encoding='utf-8'))
    raise ValueError('Tool no permitida')
if __name__=='__main__': run('security-local','1.0.0',TOOLS,handler)
