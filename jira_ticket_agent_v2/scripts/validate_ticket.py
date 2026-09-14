#!/usr/bin/env python3
import json, re, sys
from pathlib import Path

SUMMARY_RE = re.compile(r"^\[[^\]]+\]\s+DataX\s+-\s+.+\s+-\s+.+\s+-\s+Pase a producci[oó]n$", re.I)
REQ_DESC = ["Informacion General", "Proyecto Finalista", "UUAA", "Origen", "Destino"]

def result(rule, ok, evidence, action=""):
    return {"rule": rule, "result": "PASS" if ok else "FAIL", "evidence": evidence, "action": action}

def validate(data):
    out=[]
    summary=data.get("summary","")
    out.append(result("FMT-001", bool(SUMMARY_RE.match(summary)), summary, "Alinear el summary al perfil deployment-datax"))
    desc=data.get("description","")
    for name in REQ_DESC:
        out.append(result(f"DESC-{name}", name.lower() in desc.lower(), name, f"Agregar {name}"))
    readiness=data.get("readiness",{})
    for key in ["dor_complete","dod_complete","acceptance_complete"]:
        out.append(result(key.upper(), readiness.get(key) is True, str(readiness.get(key)), f"Completar {key}"))
    atts=data.get("attachments",[])
    out.append(result("ATT-PRESENT", len(atts)>0, f"{len(atts)} attachments", "Adjuntar evidencia requerida"))
    for a in atts:
        ok=bool(a.get("filename")) and int(a.get("size",0))>0
        out.append(result("ATT-META",ok,f"{a.get('filename')} size={a.get('size')}","Corregir adjunto"))
    links=data.get("links",[])
    rels={str(x.get("type","")).lower() for x in links}
    for expected in ["in deployment","is child item of","tested by"]:
        out.append(result("LINK-"+expected.upper().replace(" ","_"), expected in rels, expected, f"Agregar/verificar link {expected}"))
    subtasks=data.get("subtasks",[])
    out.append(result("SUB-PRESENT", len(subtasks)>0, f"{len(subtasks)} subtasks", "Crear/verificar subtareas requeridas"))
    for s in subtasks:
        st=str(s.get("status","")).upper()
        ok=st in {"ACCEPTED","DONE","CLOSED","RESOLVED","DEPLOYED"}
        out.append(result("SUB-STATUS",ok,f"{s.get('key')}={st}","Completar subtask bloqueante"))
    blockers=[r for r in out if r["result"]=="FAIL"]
    decision="READY" if not blockers else "NOT READY"
    return {"decision":decision,"checks":out}

def main():
    p=Path(sys.argv[1] if len(sys.argv)>1 else "demo_jira_ticket/ticket-ready.json")
    data=json.loads(p.read_text(encoding="utf-8"))
    report=validate(data)
    print(json.dumps(report,ensure_ascii=False,indent=2))
    sys.exit(0 if report["decision"]=="READY" else 2)
if __name__=="__main__": main()
