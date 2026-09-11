#!/usr/bin/env python3
import argparse, json
from pathlib import Path

def assess(inv):
    blockers=[]; adaptations=[]
    if inv.get('cics_commands'): blockers.append('Dependencia de comandos CICS: requiere separar capa de interaccion online.')
    if inv.get('has_commarea'): blockers.append('Uso de COMMAREA: definir contrato de entrada batch equivalente.')
    if inv.get('sql_tables'): adaptations.append('Definir estrategia transaccional/commit para procesamiento batch.')
    if inv.get('file_descriptors'): adaptations.append('Revisar disposicion, locking, restart/recovery e idempotencia de archivos.')
    if inv.get('calls'): adaptations.append('Confirmar que subprogramas invocados son batch-safe y reentrantes cuando aplique.')
    return {'direct_conversion_recommended': not blockers, 'blockers':blockers, 'adaptations':adaptations,
            'required_tests':['regresion funcional','volumetria','restart/recovery','idempotencia','errores y reintentos']}

def main():
    p=argparse.ArgumentParser(); p.add_argument('inventory_json'); p.add_argument('--out')
    a=p.parse_args(); r=assess(json.loads(Path(a.inventory_json).read_text())); s=json.dumps(r,indent=2,ensure_ascii=False); print(s)
    if a.out: Path(a.out).write_text(s,encoding='utf-8')
if __name__=='__main__': main()
