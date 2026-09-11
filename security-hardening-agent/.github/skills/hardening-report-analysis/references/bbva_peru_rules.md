# Baseline de Seguridad BBVA Peru - Demo

Resumen operativo de un Modelo de Seguridad BBVA Peru 2026 consultado para la demo:

- Mantener al menos entornos previos y produccion segregados; no usar datos productivos en previos salvo tratamiento/desnaturalizacion aprobada.
- Proteger datos en transito con protocolos cifrados. Evitar TELNET, HTTP y FTP cuando transporten informacion sensible; preferir SSH/HTTPS/SFTP segun arquitectura.
- Para HTTPS, el baseline observado exige TLS 1.2 o superior.
- En reposo, la referencia observada indica AES-256 GCM como minimo para la capa indicada por el modelo; evitar interpretar esto como una regla universal fuera de su alcance sin consultar Arquitectura de Seguridad.
- Mantener codigo fuente en repositorio corporativo oficial e integrado a pipeline DevOps con analisis automatizado de vulnerabilidades/calidad (referencias: Chimera/SonarQube en el documento consultado).
- Sistemas operativos/plataformas deben seguir hardening corporativo y herramientas corporativas de escaneo.
- Toda remediacion de infraestructura o produccion requiere aprobacion humana y procedimiento oficial.
