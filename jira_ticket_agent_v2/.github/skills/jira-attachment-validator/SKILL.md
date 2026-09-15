---
name: jira-attachment-validator
description: Valida adjuntos e imagenes de tickets Jira usando metadata del MCP y, cuando el contenido sea accesible, inspeccion local del archivo. Usar para verificar evidencias DQA, capturas, matrices, nombres, extensiones, tamanos, legibilidad y correspondencia con el ticket.
---
# Workflow
1. Inventariar attachments.
2. Verificar filename, extension/MIME y size > 0.
3. Clasificar el proposito probable: DQA, captura, matriz, otro.
4. Si el MCP permite descargar: guardar temporalmente y ejecutar `scripts/validate_attachment.py`.
5. Para imagenes accesibles, verificar que el archivo abra, dimensiones > 0 y formato reconocido. Evaluar contenido visual solo si realmente se puede inspeccionar.
6. Para XLSX/PDF accesibles, verificar que el archivo sea abrible; no afirmar que el contenido funcional es correcto sin revisarlo.
7. Si solo existe metadata, usar `UNKNOWN_VISUAL`, nunca PASS visual.
