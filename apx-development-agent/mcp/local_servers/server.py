#!/usr/bin/env python3
from mcp_runtime import run
from utils import run_json_script, safe_path, PROJECT

RULES=PROJECT/'.github/skills/apx-best-practices/references/bbva_peru_rules.md'
TOOLS=[
 {"name":"search_apx_baseline","description":"Busca texto en el baseline APX BBVA Perú versionado con la demo.","inputSchema":{"type":"object","properties":{"query":{"type":"string"}},"required":["query"]}},
 {"name":"validate_apx_manifest","description":"Valida tipo de recurso, jobs, rama y coverage declarada contra el baseline APX de demo.","inputSchema":{"type":"object","properties":{"manifest":{"type":"string"}},"required":["manifest"]}},
 {"name":"review_apx_repo","description":"Ejecuta revisión estructural local de un repo APX de demo.","inputSchema":{"type":"object","properties":{"repo":{"type":"string"},"branch":{"type":"string"}},"required":["repo"]}},
 {"name":"analyze_apx_dependencies","description":"Analiza POMs Maven y módulos para construir impacto técnico local.","inputSchema":{"type":"object","properties":{"repo":{"type":"string"}},"required":["repo"]}}
]

def handler(name,a):
    if name=='search_apx_baseline':
        q=a['query'].lower(); lines=[]
        for i,line in enumerate(RULES.read_text(encoding='utf-8').splitlines(),1):
            if q in line.lower(): lines.append({"line":i,"text":line})
        return {"query":a['query'],"matches":lines[:30],"baseline_only":True}
    if name=='validate_apx_manifest':
        return run_json_script('.github/skills/apx-best-practices/scripts/validate_apx_practices.py',[safe_path(a['manifest'])])
    if name=='review_apx_repo':
        args=[safe_path(a['repo'])]
        if a.get('branch'): args += ['--branch',a['branch']]
        return run_json_script('.github/skills/apx-code-review/scripts/review_apx_repo.py',args)
    if name=='analyze_apx_dependencies':
        out=safe_path('output_apx_impact_mcp.json')
        return run_json_script('.github/skills/apx-change-impact/scripts/analyze_apx_dependencies.py',[safe_path(a['repo']),'--out',out])
    raise ValueError('Tool no permitida')

if __name__=='__main__': run('apx-local','1.0.0',TOOLS,handler)
