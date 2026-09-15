#!/usr/bin/env python3
from pathlib import Path
import json, sys
ROOT=Path(__file__).resolve().parents[1]; errors=[]
required=['.github/agents/orchestration-engineer.agent.md','.github/agents/integration-specialist.agent.md','.github/agents/contract-specialist.agent.md','.github/agents/testing-specialist.agent.md','.github/agents/validation-specialist.agent.md','demo_orchestration/run/result.json','demo_orchestration/orchestration-report.html']
for r in required:
    if not (ROOT/r).exists(): errors.append('missing '+r)
skills=list((ROOT/'.github/skills').glob('*/SKILL.md'))
if len(skills)!=6: errors.append(f'expected 6 skills, found {len(skills)}')
rp=ROOT/'demo_orchestration/run/result.json'; hp=ROOT/'demo_orchestration/orchestration-report.html'
if rp.exists() and hp.exists():
    result=json.loads(rp.read_text()); h=hp.read_text()
    for p in result['packets']:
        if p['agent'] not in h: errors.append('HTML missing '+p['agent'])
    if result['final']['status'] not in h: errors.append('HTML missing final gate')
print('skills=',len(skills)); print('RESULT:','PASS' if not errors else 'FAIL')
for e in errors: print('-',e)
sys.exit(1 if errors else 0)
