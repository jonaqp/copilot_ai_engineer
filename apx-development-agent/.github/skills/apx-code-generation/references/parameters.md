# Parametros

## 1. Generar plan de trabajo

```bash
python scripts/generate_apx_workplan.py \
  --component <nombre> \
  --resource-type ud-online|ud-batch|library|dto|shell-script|statics \
  [--package <package>] \
  [--template-dir <ruta>] \
  [--out plan.json]
```

## 2. Renderizar codigo desde una plantilla aprobada

```bash
python scripts/render_from_approved_template.py \
  --template-dir <ruta_plantilla_aprobada> \
  --params <parametros.json> \
  --output-dir <destino>
```

Los placeholders soportados usan formato `{{CLAVE}}`. El script falla si falta un parametro o si intenta sobrescribir un archivo sin `--overwrite`.

La Skill **no inventa APIs APX**. Para generar codigo real debe existir un patron/plantilla aprobada o un componente equivalente en el repositorio.
