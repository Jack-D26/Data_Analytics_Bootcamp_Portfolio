# Sprint_14_Proyecto_Final_Modular

Este repositorio forma parte de la entrega del proyecto final del Sprint 14 del bootcamp de análisis de datos.  
El objetivo del proyecto es analizar el desempeño operativo de un servicio de telefonía virtual (CallMeMaybe) para identificar posibles áreas de mejora.

El análisis se desarrolló inicialmente en un Jupyter Notebook (`.ipynb`), pero esta versión ha sido **modularizada** en distintos scripts de Python organizados por función, lo que permite un mantenimiento más limpio y profesional.

---

## Estructura inicial del proyecto

```plaintext
Sprint_14_Proyecto_Final_Modular/
├── data/
├── docs/
│   └── report.md
├── notebooks/
│   └── Proyecto_Final_Sprint_14_*.ipynb
├── scripts/
│   ├── eda/
│   ├── identificacion_ineficaces/
│   ├── load_data.py
│   ├── preprocessing.py
│   ├── pruebas_hipotesis.py
│   └── visualizaciones.py
├── run_pipeline.py
├── requirements.txt
└── README.md

```

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

> 💡 Todas las dependencias entre scripts (como columnas requeridas) están gestionadas automáticamente por `run_pipeline.py`. No es necesario importar funciones manualmente ni ejecutar celdas paso a paso.

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

### Lo que se incluye en esta fase

Top 15 operadores con más llamadas perdidas (con y sin NA)

Distribución de tiempos de espera por operador

Matriz de correlación entre variables clave

Histograma de llamadas salientes

Tablas de clasificación de operadores (ranking)

Comparación agregada por plan tarifario
