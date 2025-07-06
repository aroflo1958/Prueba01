# Prueba01
Aplicación para uso médico destinada a analizar los datos del paciente y
determinar si cumple criterios para el diagnóstico de EPOC (Enfermedad
Pulmonar Obstructiva Crónica) según la clasificación y manejo descritos en la
"Guía de la iniciativa GOLD 2025.pdf". Una vez confirmado el diagnóstico, el
objetivo es clasificar la severidad y sugerir un plan de tratamiento de acuerdo
con las recomendaciones internacionales.

## Instrucciones de instalación

1. **Clonar el repositorio**:

   ```bash
   git clone <url-del-repositorio>
   cd Prueba01
   ```

2. **Instalar dependencias** (requiere Python 3.9 o superior):

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt  # en caso de que existan dependencias
   ```

3. **Preparar los datos del paciente** en un archivo de texto o en un formato
   estructurado (por ejemplo, CSV) siguiendo los campos descritos a
   continuación.

## Campos requeridos de datos del paciente

Los datos utilizados para determinar la severidad de EPOC deben incluir:

| Campo                     | Descripción                                                                            |
|---------------------------|----------------------------------------------------------------------------------------|
| `FEV1`                    | Volumen espiratorio forzado en el primer segundo (expresado en litros o en % del predicho). |
| `FVC`                     | Capacidad vital forzada.                                                                |
| `FEV1/FVC`                | Relación entre FEV1 y FVC. Un valor <70% sugiere obstrucción.                          |
| `puntaje_symptom`         | Escala de síntomas (por ejemplo, CAT o mMRC).                                          |
| `historia_tabaquismo`     | Número de paquetes/año fumados.                                                        |
| `exacerbaciones_previas`  | Número de exacerbaciones en el último año.                                             |

Estos campos permiten clasificar la enfermedad de acuerdo con la
estratificación propuesta en la guía GOLD 2025, que combina la función
pulmonar (FEV1) y la carga de síntomas.

## Interpretación de la salida

Al ejecutar el programa con los datos anteriores, el sistema debe devolver un
informe con dos elementos principales:

1. **Confirmación del diagnóstico** de EPOC si la relación `FEV1/FVC` es inferior
   al 70% y existe exposición a factores de riesgo (por ejemplo, tabaquismo).
2. **Clasificación de severidad** según el valor de `FEV1` y el puntaje de
   síntomas. Por ejemplo, la guía GOLD 2025 establece las categorías A, B, C y D,
   que combinan el grado de obstrucción con el nivel de síntomas y el historial
   de exacerbaciones.

La salida puede incluir recomendaciones generales de tratamiento basadas en la
categoría asignada. Para un detalle completo, consulte la **Guía de la
iniciativa GOLD 2025**, la cual proporciona los algoritmos y tablas de manejo
actualizados.

## Transparencia

Esta aplicación sigue las recomendaciones descritas en la versión 2025 del
GOLD (Global Initiative for Chronic Obstructive Lung Disease). Se invita a los
usuarios a revisar dicha guía para comprender el contexto y la justificación de
cada criterio.

