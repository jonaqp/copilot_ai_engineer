#!/usr/bin/env python3
from mcp_runtime import run
from utils import run_json_script, safe_path

TOOLS=[
 {"name":"analyze_cobol","description":"Analiza un fuente COBOL local y extrae PROGRAM-ID, CALL, COPY, SQL y CICS.","inputSchema":{"type":"object","properties":{"source":{"type":"string"}},"required":["source"]}},
 {"name":"validate_host_release","description":"Valida un manifiesto local de release Host contra el baseline DQA Perú de demo.","inputSchema":{"type":"object","properties":{"manifest":{"type":"string"}},"required":["manifest"]}},
 {"name":"build_host_dependency_graph","description":"Construye dependencias CALL/COPY en una carpeta COBOL local.","inputSchema":{"type":"object","properties":{"root":{"type":"string"}},"required":["root"]}}
]

def handler(name,a):
    if name=="analyze_cobol":
        return run_json_script('.github/skills/host-code-analysis/scripts/analyze_cobol.py',[safe_path(a['source'])])
    if name=="validate_host_release":
        return run_json_script('.github/skills/host-release-readiness/scripts/validate_host_release.py',[safe_path(a['manifest'])])
    if name=="build_host_dependency_graph":
        out=safe_path('output_host_dependencies.json')
        return run_json_script('.github/skills/host-dependency-impact/scripts/build_dependency_graph.py',[safe_path(a['root']),'--out',out])
    raise ValueError('Tool no permitida')

if __name__=='__main__': run('host-local','1.0.0',TOOLS,handler)
