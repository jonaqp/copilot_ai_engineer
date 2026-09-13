# Prompts de ejemplo — Impact Radar

## 1. Primer análisis visual

```text
Analiza el impacto de cambiar el contrato de pricing-service.
Actualiza demo_arch_radar/static-demo.html reemplazando la versión anterior.
El grafo debe reflejar ROOT, L1, L2+, dependencias ocultas, risk score,
decisión Shift-Left y validaciones. Ejecuta la validación del HTML al terminar.
```

## 2. Cambiar el escenario y sobrescribir el mismo HTML

```text
Ahora analiza un cambio schema en order-db.
No crees otro HTML. Regenera static-demo.html para que deje de mostrar
pricing-service y muestre únicamente el nuevo escenario de order-db.
```

## 3. Mejorar el radar progresivamente

```text
Mejora el radar agregando agrupación visual por owner y una leyenda de criticidad.
Haz la mejora en la plantilla/CSS/JS para que sea persistente.
Después regenera static-demo.html usando el escenario actual y valida el resultado.
```

## 4. Volver al estado base

```text
Restablece la demo visual al modo BASE sin componente raíz seleccionado.
Regenera static-demo.html y valida que impactData sea null.
```
