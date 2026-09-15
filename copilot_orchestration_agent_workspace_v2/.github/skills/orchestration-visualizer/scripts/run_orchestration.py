#!/usr/bin/env python3
from __future__ import annotations
import asyncio, json, subprocess, sys, time, html
from pathlib import Path
from datetime import datetime, timezone
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
DEMO=ROOT/'demo_orchestration'; RUN=DEMO/'run'; RUN.mkdir(parents=True,exist_ok=True)
def now(): return datetime.now(timezone.utc).isoformat()
def packet(agent,status,start,checks,evidence=None,risks=None):
    return {'run_id':RUN_ID,'agent':agent,'status':status,'started_at':start,'finished_at':now(),'duration_ms':int((time.perf_counter()-STARTS[agent])*1000),'checks':checks,'evidence':evidence or [],'risks':risks or [],'files_changed':[]}
async def contract_agent():
    agent='contract-specialist'; STARTS[agent]=time.perf_counter(); start=now(); await asyncio.sleep(.10)
    base=DEMO/'superstore/contracts'; req=json.loads((base/'order-request.json').read_text()); rsp=json.loads((base/'order-response.json').read_text())
    checks=[{'id':'request-required','status':'PASS' if set(req['required'])=={'sku','qty','payment_token'} else 'FAIL','summary':'Required request fields match checkout inputs'},{'id':'response-status','status':'PASS' if {'CONFIRMED','REJECTED'}<=set(rsp['allowed_status']) else 'FAIL','summary':'Response statuses cover service outcomes'}]
    return packet(agent,'PASS' if all(c['status']=='PASS' for c in checks) else 'FAIL',start,checks,[str(base/'order-request.json'),str(base/'order-response.json')])
async def integration_agent():
    agent='integration-specialist'; STARTS[agent]=time.perf_counter(); start=now(); await asyncio.sleep(.14)
    cfg=json.loads((DEMO/'superstore/config/integrations.json').read_text()); deps=cfg['order-service']['depends_on']; expected={'catalog-service','inventory-service','payment-service'}
    checks=[{'id':'dependency-map','status':'PASS' if set(deps)==expected else 'FAIL','summary':f"order-service dependencies: {', '.join(deps)}"}]
    try:
        from demo_orchestration.superstore.services.orders import checkout
        r=checkout('KB-01',1,'tok_smoke'); ok=r.get('status')=='CONFIRMED'
    except Exception as e: ok=False; r={'error':str(e)}
    checks.append({'id':'checkout-smoke','status':'PASS' if ok else 'FAIL','summary':str(r)})
    return packet(agent,'PASS' if all(c['status']=='PASS' for c in checks) else 'FAIL',start,checks,[str(DEMO/'superstore/config/integrations.json')])
async def testing_agent():
    agent='testing-specialist'; STARTS[agent]=time.perf_counter(); start=now(); await asyncio.sleep(.05)
    cmd=[sys.executable,'-m','unittest','discover','-s','demo_orchestration/superstore/tests','-p','test_*.py']; p=await asyncio.to_thread(subprocess.run,cmd,cwd=ROOT,text=True,capture_output=True)
    checks=[{'id':'functional-regression','status':'PASS' if p.returncode==0 else 'FAIL','summary':(p.stdout+p.stderr).strip()[-1200:],'command':' '.join(cmd)}]
    return packet(agent,'PASS' if p.returncode==0 else 'FAIL',start,checks,['demo_orchestration/superstore/tests/test_order_flow.py'])
async def validation_agent(packets):
    agent='validation-specialist'; STARTS[agent]=time.perf_counter(); start=now(); await asyncio.sleep(.04)
    states={p['agent']:p['status'] for p in packets}; required=['contract-specialist','integration-specialist','testing-specialist']; missing=[a for a in required if a not in states]; failed=[a for a,s in states.items() if s=='FAIL']; blocked=[a for a,s in states.items() if s in {'BLOCKED','UNKNOWN'}]
    status='FAIL' if failed or missing else ('PASS WITH CONDITIONS' if blocked else 'PASS')
    checks=[{'id':'all-required-agents','status':'PASS' if not missing else 'FAIL','summary':f"missing={missing or 'none'}"},{'id':'critical-results','status':'PASS' if not failed else 'FAIL','summary':f"failed={failed or 'none'}"}]
    return packet(agent,status,start,checks,risks=[f'blocked={blocked}'] if blocked else [])
def make_html(result):
    state={'PASS':'pass','FAIL':'fail','BLOCKED':'blocked','UNKNOWN':'unknown','PASS WITH CONDITIONS':'warn'}; packets=result['packets']; cards=[]
    for p in packets:
        checks=''.join('<li><span class="dot %s"></span><b>%s</b> — %s</li>'%(state.get(c['status'],'unknown'),html.escape(c['id']),html.escape(c['summary'])) for c in p['checks'])
        cards.append('<article class="agent-card"><div class="card-top"><div><div class="eyebrow">SUBAGENT</div><h3>%s</h3></div><span class="pill %s">%s</span></div><div class="time">%s ms</div><ul>%s</ul></article>'%(html.escape(p['agent']),state.get(p['status'],'unknown'),html.escape(p['status']),p['duration_ms'],checks))
    final=result['final']; lanes=''.join('<div class="lane"><span>%s</span><b>%s</b><em>%s ms</em><strong class="%s">%s</strong></div>'%(i+1,html.escape(p['agent']),p['duration_ms'],state.get(p['status'],'unknown'),html.escape(p['status'])) for i,p in enumerate(packets[:3])); data=json.dumps(result,ensure_ascii=False).replace('</','<\\/')
    return '''<!doctype html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Copilot Multi-Agent Orchestration</title><style>*{box-sizing:border-box}body{margin:0;font-family:Inter,system-ui,Segoe UI,sans-serif;background:#07111f;color:#eaf2ff}.wrap{max-width:1280px;margin:auto;padding:36px 24px 64px}h1{font-size:clamp(34px,5vw,68px);margin:8px 0}.subtitle{color:#9fb3ca;max-width:850px;font-size:18px}.hero{background:linear-gradient(135deg,#0c2038,#11182b);border:1px solid #203d5c;border-radius:24px;padding:28px}.eyebrow{font-size:11px;letter-spacing:.18em;color:#6ee7ff}.grid{display:grid;grid-template-columns:1.2fr .8fr;gap:20px;margin-top:20px}.panel,.agent-card{background:#0c1728;border:1px solid #1c3551;border-radius:18px;padding:20px}.wave{display:grid;gap:12px}.lane{display:grid;grid-template-columns:32px 1fr auto auto;align-items:center;gap:12px;background:#101f34;padding:14px;border-radius:12px}.lane>span{width:28px;height:28px;border-radius:50%%;display:grid;place-items:center;background:#18324e}.lane em{color:#8da6bd}.arrow{text-align:center;color:#6ee7ff;font-size:28px;padding:6px}.fan{display:flex;gap:10px;align-items:center;justify-content:center;background:#101f34;padding:18px;border-radius:14px}.pill,.fan strong{padding:7px 10px;border-radius:999px;font-size:12px}.pass{color:#68f0b0}.fail{color:#ff6b7b}.warn{color:#ffd166}.blocked,.unknown{color:#aab9ca}.pill.pass{background:#123c31}.pill.fail{background:#4a1d29}.pill.warn{background:#43391b}.agents{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:16px;margin-top:20px}.card-top{display:flex;justify-content:space-between;gap:14px}.agent-card h3{margin:5px 0}.time{color:#7f96ad;font-size:12px}ul{padding-left:18px;color:#b9c8d8}li{margin:10px 0}.dot{display:inline-block;width:8px;height:8px;border-radius:50%%;background:currentColor;margin-right:8px}.kpi{font-size:52px;font-weight:800}code{color:#9ee7ff}@media(max-width:850px){.grid,.agents{grid-template-columns:1fr}.lane{grid-template-columns:32px 1fr}.lane em,.lane strong{grid-column:2}}</style></head><body><main class="wrap"><section class="hero"><div class="eyebrow">GITHUB COPILOT · MULTI-AGENT CONTROL PLANE</div><h1>Orchestration Radar</h1><p class="subtitle">Fan-out paralelo, evidencia aislada por subagente y fan-in de validación. El dashboard se regenera desde el resultado real de cada ejecución.</p></section><section class="grid"><div class="panel"><div class="eyebrow">WAVE 1 · PARALLEL FAN-OUT</div><h2>3 subagentes simultáneos</h2><div class="wave">%s</div><div class="arrow">↓ &nbsp; ↓ &nbsp; ↓</div><div class="fan"><span>FAN-IN</span><b>validation-specialist</b><strong class="%s">%s</strong></div></div><div class="panel"><div class="eyebrow">FINAL GATE</div><div class="kpi %s">%s</div><p>Run ID: <code>%s</code></p><p>Parallel wall time: <b>%s ms</b></p><p>Sequential sum: <b>%s ms</b></p><p>Ahorro ilustrativo por paralelismo: <b>%s ms</b></p></div></section><section class="agents">%s</section><script id="runData" type="application/json">%s</script></main></body></html>'''%(lanes,state.get(final['status'],'unknown'),html.escape(final['status']),state.get(final['status'],'unknown'),html.escape(final['status']),html.escape(result['run_id']),result['parallel_wall_ms'],result['sequential_sum_ms'],max(0,result['sequential_sum_ms']-result['parallel_wall_ms']),''.join(cards),data)
async def main():
    global RUN_ID, STARTS
    RUN_ID=datetime.now(timezone.utc).strftime('run-%Y%m%dT%H%M%SZ'); STARTS={}; plan={'run_id':RUN_ID,'goal':'Validate SuperStore checkout change before merge','waves':[{'id':'wave-1','parallel':True,'tasks':['contract-specialist','integration-specialist','testing-specialist']},{'id':'wave-2','parallel':False,'tasks':['validation-specialist']}]}; (RUN/'plan.json').write_text(json.dumps(plan,indent=2),encoding='utf-8')
    wall=time.perf_counter(); packets=list(await asyncio.gather(contract_agent(),integration_agent(),testing_agent())); parallel_wall=int((time.perf_counter()-wall)*1000); final=await validation_agent(packets); allp=packets+[final]
    result={'run_id':RUN_ID,'plan':plan,'packets':allp,'final':{'agent':final['agent'],'status':final['status'],'checks':final['checks']},'parallel_wall_ms':parallel_wall,'sequential_sum_ms':sum(p['duration_ms'] for p in packets)}; (RUN/'result.json').write_text(json.dumps(result,indent=2),encoding='utf-8'); (DEMO/'orchestration-report.html').write_text(make_html(result),encoding='utf-8')
    print('RUN:',RUN_ID)
    for p in allp: print(f"{p['agent']:<28} {p['status']:<20} {p['duration_ms']:>4} ms")
    print('FINAL:',final['status']); print('REPORT:',DEMO/'orchestration-report.html'); return 0 if final['status']=='PASS' else 1
if __name__=='__main__': raise SystemExit(asyncio.run(main()))
