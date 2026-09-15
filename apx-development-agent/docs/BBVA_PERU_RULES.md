# Baseline APX / BBVA Peru

Resumen de reglas internas usadas por esta demo. Validar vigencia antes de produccion.

## Gobierno y ciclo
- APX se documenta como Architecture Platform extended dentro de ETHER Software Development Platform.
- Modelo de gobierno observado: Diseno -> Construccion -> Despliegue.
- Tipologias Jira observadas: alta de componente, modificacion de componente y modificacion express para casos acotados.

## Recursos y estructura
- Recursos APX observados: UD Online, UD Batch, Libreria, DTO, Shell Script y Estaticos.
- Una UD agrupa componentes con el mismo ciclo de vida; una UD Batch contiene un unico job.
- La estructura de UD incluye `artifact/`, `doc/`, `.gitignore`, `pom.xml` y metadatos/pipeline de plataforma (`apx.json` en recursos modernos segun la referencia).
- Preferir CLI APX aprobado para manipular artefactos; no inventar estructura si el repositorio ya tiene una plantilla vigente.

## Ramas y CI
- Baseline documentado desde 2022: modelo gitflow unificado; `develop` como origen; `feature` para trabajo; `bugfix` sobre release no productiva; `hotfix` para release ya productiva.
- Pipeline observado: controles/gobierno, build, tests unitarios, Sonar, publicacion de artefactos y trazabilidad.
- Controles mencionados: SonarQube y deteccion de vulnerabilidades mediante Chimera.

## Testing
- Baseline APX documentado: cobertura de al menos 80% sobre nuevo codigo; el Quality Gate puede impedir el pipeline si no se alcanza.
- Esta demo solo puede calcular cobertura global cuando recibe XML/LCOV; no debe afirmar cobertura de nuevo codigo si el reporte no la distingue.

## Regla de seguridad
- No generar llamadas a APIs APX propietarias por memoria. Inferir patrones del repositorio actual o usar plantillas/documentacion aprobadas.
