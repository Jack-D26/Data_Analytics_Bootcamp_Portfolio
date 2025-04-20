# Proyecto S7 – Aplicación Web de Análisis Exploratorio con Streamlit 🚗

**[Haz clic aquí para ver la app en vivo en Render →](https://app-exploratory-analysis.onrender.com)**

Este repositorio contiene el proyecto desarrollado como parte del **Sprint 7** del bootcamp de análisis de datos. El objetivo principal fue construir y desplegar una aplicación web interactiva utilizando `Streamlit`, enfocada en la exploración visual del conjunto de datos `vehicles_us.csv`.

---

## Objetivo del Proyecto

Aplicar herramientas de desarrollo de software y despliegue web para construir una app sencilla pero funcional que permita:

- Visualizar la relación entre el precio y el kilometraje de vehículos usados.
- Explorar de forma interactiva los datos con histogramas y gráficos de dispersión.
- Desplegar la aplicación en la nube (Render.com) como producto final.

Este proyecto demuestra cómo convertir un análisis exploratorio inicial en una herramienta web interactiva simple, funcional y visualmente clara.

---

## Dataset utilizado

El conjunto de datos utilizado es `vehicles_us.csv`, el cual contiene información sobre anuncios de venta de autos en Estados Unidos. Incluye variables como:

- Precio (`price`)
- Kilometraje (`odometer`)
- Tipo de transmisión
- Año del vehículo
- Tipo de combustible
- Entre otros

---

## Funcionalidades de la app

La aplicación, construida con `Streamlit`, incluye:

- Un **histograma interactivo** para explorar el kilometraje (`odometer`)
- Un **gráfico de dispersión** para analizar la relación entre kilometraje y precio
- Controles mediante **checkboxes** para activar/desactivar las visualizaciones

---

## Estructura del repositorio

Proyecto_S7_Vehicles_app/ ├── vehicles_app.py # Código principal de la aplicación Streamlit ├── data/ │ └── vehicles_us.csv # Dataset base ├── notebooks/ │ └── EDA.ipynb # Análisis exploratorio inicial ├── requirements.txt # Librerías necesarias ├── .gitignore # Archivos excluidos del repositorio └── README.md # Este archivo

## ¿Cómo ejecutar la app?

1. Clona este repositorio:

```bash
git clone https://github.com/Jack-D26/Proyecto_S7_Vehicles_app.git
cd Proyecto_S7_Vehicles_app
```

2. Crea un entorno virtual (opcional pero recomendado):

python -m venv venv
source venv/bin/activate # Linux / Mac
.\venv\Scripts\activate # Windows

3. Instala las dependencias:

pip install -r requirements.txt

4. Ejecuta la aplicación:

streamlit run vehicles_app.pygit status
