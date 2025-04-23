# Sprint_14_Proyecto_Final_Modular

Este repositorio forma parte de la entrega del proyecto final del Sprint 14 del bootcamp de análisis de datos.  
El objetivo del proyecto es analizar el desempeño operativo de un servicio de telefonía virtual (CallMeMaybe) para identificar posibles áreas de mejora.

El análisis se desarrolló inicialmente en un Jupyter Notebook (`.ipynb`), pero esta versión ha sido **modularizada** en distintos scripts de Python organizados por función, lo que permite un mantenimiento más limpio y profesional.

---

## Estructura inicial del proyecto

    Sprint_14_Proyecto_Final_Modular/

├── data/ # Datasets u outputs opcionales
├── docs/ # Reporte en Markdown, gráficos (próximamente)
│ └── report.md
├── notebooks/ # Notebook original del proyecto
├── scripts/ # Scripts modulares por etapa
│ ├── eda/ # EDA segmentado por tema
│ ├── identificacion_ineficaces/ # Clasificación de desempeño
│ ├── load_data.py
│ ├── preprocessing.py
│ ├── pruebas_hipotesis.py
│ └── visualizaciones.py
├── run_pipeline.py # Pipeline maestro que orquesta todo
├── requirements.txt
└── README.md

---

## ¿Qué hace el pipeline?

run_pipeline.py ejecuta toda la cadena de análisis:

Carga de datos desde URLs públicas

Preprocesamiento y limpieza de nulos y duplicados

Generación de columnas clave como duración y espera

EDA modular: outliers, tiempos, planes, pérdidas

Cálculo de métricas por operador

Clasificación por eficiencia (basado en umbrales dinámicos)

Visualizaciones exploratorias y ejecutivas

Pruebas de hipótesis para validar insights

Reporte automático guardado como docs/report.md

---

## ¿Cómo correrlo?

### Clona el repositorio y entra al directorio:

git clone <https://github.com/Jack-D26/Data_Analytics_Bootcamp_Portfolio>

cd Sprint_14_Proyecto_Final_Modular

### Crea un entorno virtual (opcional):

python -m venv venv
source venv/bin/activate # Mac/Linux
venv\Scripts\activate # Windows

### Instala las dependencias:

pip install -r requirements.txt

### Ejecuta el pipeline:

python run_pipeline.py

---

## Salida del pipeline

🖥️ Imprime estadísticas, resultados y pruebas al terminal

📝 Genera automáticamente un reporte en docs/report.md

📊 Muestra visualizaciones en pantalla (se pueden guardar opcionalmente)

📁 (Próximamente) Exportación de CSVs y gráficos a /data y /docs/figures

---

## Créditos

Desarrollado por [Joako] en el marco del proyecto final de Sprint 14, con el soporte técnico de Data_Partner.

---

## Etapa de Análisis Exploratorio de Datos (EDA)

Se completó la etapa de EDA con una **modularización del análisis**, separando las funciones clave en scripts individuales dentro del directorio `/scripts`.

Esto permite mantener un código limpio, reutilizable y más fácil de escalar o modificar.

### Scripts creados

| Script                     | Descripción                                                            |
| -------------------------- | ---------------------------------------------------------------------- |
| `eda_outliers.py`          | Análisis y visualización de outliers por plan tarifario                |
| `eda_planes.py`            | Distribución de llamadas atípicas por tipo de plan tarifario           |
| `eda_operadores.py`        | Métricas agregadas por operador (llamadas, espera, duración, pérdidas) |
| `eda_tiempos.py`           | Análisis de duración de llamadas y tiempos de espera                   |
| `eda_llamadas_perdidas.py` | Bin de tiempos de espera y proporción de llamadas perdidas             |

### 🔄 Orden sugerido de ejecución

1. `eda_outliers.py`
2. `eda_planes.py`
3. `eda_operadores.py`
4. `eda_tiempos.py`
5. `eda_llamadas_perdidas.py`

---

> Para ejecutar los análisis, asegúrate de tener cargados `df_calls`, `df_clients`, y haber aplicado el preprocesamiento previo. Cada módulo puede ser importado o ejecutado de manera individual.

---

## Identificación de Operadores Ineficientes

Esta fase tiene como objetivo identificar a los operadores con bajo desempeño mediante métricas clave y criterios definidos. El análisis incluye la creación de flags de ineficiencia, la visualización de resultados y un resumen interpretativo de los hallazgos.

### Scripts involucrados (ubicados en scripts/identificacion_ineficaces/):

#### metrics_operadores.py

Contiene funciones para calcular las métricas clave por operador, así como para agregar la información del plan tarifario de cada uno.

#### umbral_ineficiencia.py

Define los umbrales que determinan cuándo un operador es considerado ineficiente, según:

Tasa de llamadas perdidas

Tiempo de espera promedio

Número de llamadas salientes

#### ineficiencia_visuals.py

Genera visualizaciones relacionadas con:

Proporción de ineficientes vs eficientes

Distribución por plan tarifario

Criterios de ineficiencia cumplidos

Histograma de carga operativa

#### resumen_ineficiencia.py

Calcula estadísticas globales (como proporción de ineficiencia) y destaca hallazgos relevantes del análisis, como sobrecarga por plan tarifario.

### Cómo ejecutar esta fase

En tu notebook principal, importa las funciones de la siguiente manera:

from scripts.identificacion_ineficaces.metrics_operadores import (
calcular_metricas_por_operador,
agregar_plan_tarifario
)
from scripts.identificacion_ineficaces.umbral_ineficiencia import (
calcular_umbral_ineficiencia,
etiquetar_ineficiencia
)
from scripts.identificacion_ineficaces.ineficiencia_visuals import (
plot_ineficientes_por_criterios,
plot_ineficiencia_por_plan,
plot_torta_ineficiencia,
plot_hist_total_llamadas,
plot_criterios_mas_frecuentes
)
from scripts.identificacion_ineficaces.resumen_ineficiencia import (
calcular_resumen_ineficiencia
)

Luego, puedes ejecutar paso a paso la lógica como se planteó originalmente en el .ipynb para obtener métricas, aplicar criterios y visualizar resultados.

### Requisitos previos para ejecutar esta fase

Para poder utilizar los scripts de la fase de Identificación de operadores ineficientes, es necesario que el DataFrame de llamadas (df) ya cuente con las siguientes columnas generadas previamente durante la fase de preprocesamiento y EDA:

missed_call: Columna booleana que indica si la llamada fue perdida (True si el tiempo de espera fue mayor a 0 y la duración de la llamada es 0).

wait_time: Tiempo de espera antes de ser atendido (en segundos).

call_duration: Duración total de la llamada (en segundos).

direction: Dirección de la llamada ('in' o 'out').

user_id: Identificador único del operador (necesario para hacer merge con el plan tarifario desde df_clients).

Estas columnas se generan mediante scripts de la fase de EDA ubicados en scripts/eda/.
Asegúrate de haber ejecutado los siguientes scripts antes de esta etapa:

eda_llamadas_perdidas.py

eda_tiempos.py

---

---

## Pruebas de hipótesis

El script `pruebas_hipotesis.py` contiene una serie de análisis estadísticos diseñados para validar suposiciones clave sobre el comportamiento de los operadores, como:

- Relación entre número de llamadas entrantes y tasa de abandono.
- Asociación entre tiempo de espera promedio y pérdida de llamadas.
- Comparación del desempeño entre planes tarifarios mediante Kruskal-Wallis.
- Análisis de eficiencia en función de la antigüedad de los operadores.
- Comparación entre operadores eficientes e ineficientes usando pruebas de Mann-Whitney.

### Tabla de hipótesis

| Hipótesis                                                             | Prueba aplicada | Variable principal                  |
| --------------------------------------------------------------------- | --------------- | ----------------------------------- |
| Mayor volumen de llamadas entrantes genera mayor tasa de abandono     | Pearson         | `missed_rate` vs. `total_incoming`  |
| Mayor tiempo de espera se relaciona con más abandono                  | Pearson         | `missed_rate` vs. `wait_time_mean`  |
| El plan tarifario afecta la tasa de llamadas perdidas                 | Kruskal-Wallis  | `missed_rate` por plan              |
| La antigüedad del operador impacta su eficiencia                      | Pearson         | `missed_rate` vs. antigüedad (días) |
| Existen diferencias claras entre operadores eficientes e ineficientes | Mann-Whitney    | `missed_rate` y `avg_wait_time`     |

#### Cómo ejecutar esta fase

Asegúrate de contar con los DataFrames `operator_perf`, `df_clients` y `df_calls_no_outliers`.

```python
from scripts.pruebas_hipotesis import *

prueba_correlacion_entrantes_missed(operator_perf)
prueba_correlacion_espera_missed(df_calls_no_outliers, operator_perf)
prueba_planes_tarifarios(df_calls_no_outliers, df_clients)
prueba_antiguedad_eficiencia(df_calls_no_outliers, df_clients, operator_perf)
prueba_comparacion_operadores(operator_perf)
```

---

## Visualización y Presentación de Resultados

Esta fase incluye la generación de gráficos y tablas clave que resumen el desempeño de los operadores, identifican patrones operativos y respaldan los hallazgos obtenidos en las fases anteriores. No depende de funciones externas, pero requiere que los DataFrames utilizados ya contengan las columnas generadas previamente (ver fase de identificación).

### Requisitos previos

El DataFrame principal (operator_perf) debe contener al menos las siguientes columnas:

operator_id

missed_calls

missed_rate

avg_wait_time

avg_call_duration

total_calls, total_incoming, total_outgoing

ineficiente_missed, ineficiente_wait, ineficiente_outgoing

criterios_cumplidos, es_ineficiente

tariff_plan

Además, se usa df_calls_no_outliers para obtener datos crudos y construir ciertos gráficos como la distribución de tiempos de espera.

### Lo que se incluye en esta fase

Top 15 operadores con más llamadas perdidas (con y sin NA)

Distribución de tiempos de espera por operador

Matriz de correlación entre variables clave

Histograma de llamadas salientes

Tablas de clasificación de operadores (ranking)

Comparación agregada por plan tarifario

### Ejecución

Puedes ejecutar el script completo de esta fase tras haber corrido los scripts de identificación. Asegúrate de tener cargado operator_perf con las columnas listadas arriba, y df_calls_no_outliers si aplicas los gráficos detallados.
