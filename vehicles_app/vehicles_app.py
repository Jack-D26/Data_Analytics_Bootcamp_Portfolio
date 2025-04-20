import pandas as pd
import plotly.express as px
import streamlit as st

# Cargar datos del archivo CSV
car_data = pd.read_csv('data/vehicles_us.csv')

st.header("Análisis Exploratorio de Datos del Dataset vehicles_us.csv")

# Casilla de verificación para mostrar histograma
hist_checkbox = st.checkbox('Mostrar histograma del odómetro')

if hist_checkbox:
    st.write('Creación de un histograma para los kilómetros recorridos')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

# Casilla de verificación para mostrar gráfico de dispersión
scatter_checkbox = st.checkbox(
    'Mostrar gráfico de dispersión precio vs. odómetro')

if scatter_checkbox:
    st.write(
        'Creación de un gráfico de dispersión para el precio y los kilómetros recorridos')
    fig = px.scatter(car_data, x="odometer", y="price",
                     title="Relación entre kilómetros recorridos y precio")
    st.plotly_chart(fig, use_container_width=True)
