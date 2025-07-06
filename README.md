# Prueba01

Aplicación para uso médico que analiza los datos del paciente aportados por el clínico.
Primero define si cumple criterios para el diagnóstico de EPOC (Enfermedad Pulmonar
Obstructiva Crónica) y, en caso afirmativo, la clasifica según la guía GOLD 2025.

## Requisitos

Se requiere Python 3.8 o superior.

## Uso

El análisis puede ejecutarse desde la línea de comandos con el script `copd_cli.py`:

```bash
python copd_cli.py --fev1 1.2 --fvc 3.0 --fev1_percent 55
```

La salida muestra si el paciente tiene EPOC y su clasificación GOLD.

## Referencia

Los criterios usados se basan en la "Guía de la iniciativa GOLD 2025" incluida en este
repositorio.

