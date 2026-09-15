#!/usr/bin/env python3
import argparse, json
from pathlib import Path

def main():
    p=argparse.ArgumentParser(description='Genera plan de trabajo APX sin inventar APIs propietarias')
    p.add_argument('--component',required=True); p.add_argument('--resource-type',required=True,choices=['ud-online','ud-batch','library','dto','shell-script','statics']); p.add_argument('--package'); p.add_argument('--template-dir'); p.add_argument('--out',default='apx_generation_plan.json'); a=p.parse_args()
    plan={'component':a.component,'resource_type':a.resource_type,'package':a.package,'template_dir':a.template_dir,'steps':['Inspeccionar estructura y componentes equivalentes en el repositorio','Confirmar ticket/gobierno aplicable','Reutilizar plantilla APX aprobada; no inventar APIs','Crear o modificar codigo y pruebas','Ejecutar build/tests','Validar Sonar/Chimera/quality gates disponibles','Preparar PR y evidencia'],'guardrail':'Si no hay template o patron equivalente, detener la generacion de codigo propietario y solicitar referencia aprobada.'}
    Path(a.out).write_text(json.dumps(plan,indent=2,ensure_ascii=False),encoding='utf-8'); print(json.dumps(plan,indent=2,ensure_ascii=False))
if __name__=='__main__':main()
