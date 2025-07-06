# Prueba01

Aplicación para uso médico: analizar los datos del paciente aportados por el médico y definir si llena criterios para el diagnóstico de EPOC (Enfermedad Pulmonar Obstructiva Crónica) y clasificarla. Debe usar los datos aportados por la "Guía de la iniciativa GOLD 2025.pdf".

## Uso del módulo `copd_analyzer`

La lógica principal se encuentra en `src/copd_analyzer.py`. Para invocar el módulo desde otra parte de la aplicación:

```python
from src.copd_analyzer import diagnose

paciente = {
    "fev1_fvc": 0.65,
    "fev1_percent_predicted": 85,
    "symptom_score": 1,
    "exacerbations_last_year": 0,
    "hospitalizations_last_year": 0,
}

resultado = diagnose(paciente)
print(resultado)
# {'diagnosis': True, 'gold_stage': 1, 'risk_group': 'A'}
```

## Pruebas

Las pruebas unitarias se encuentran en `tests/` y usan `pytest`.
Para ejecutarlas:

```bash
pytest
```
