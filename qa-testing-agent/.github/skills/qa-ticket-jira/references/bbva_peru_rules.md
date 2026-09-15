# Baseline BBVA Peru - DQA PE 2026

Para la demo se aplican los siguientes criterios observados en los lineamientos DQA PE:

- La HU de certificacion debe estar preparada con Summary, estado Ready, tipo Story/Bug segun aplique, labels, Team Backlog, Feature Link, Item Type Technical, Tech Stack, DoR, DoD, criterios de aceptacion, Story Points, Sprint, descripcion, evidencias y Fix Version cuando aplique.
- Se debe ejecutar Jira Validator y adjuntar evidencia satisfactoria.
- Xray: enlazar Test con evidencias; cada Test debe contar con Test Execution; cada Test Execution debe tener evidencia por fuente; Test y Test Execution se manejan en estado New en el flujo descrito.
- PR: asociar a HU de certificacion; contar con aprobaciones requeridas; ultima build Passed; validaciones de plataforma/BOT y Sonar cuando apliquen; commits vinculados a HUs.
- No realizar merge si las aprobaciones obligatorias aun no estan aceptadas.
- Validar siempre la plantilla DQA vigente antes de crear tickets reales.
