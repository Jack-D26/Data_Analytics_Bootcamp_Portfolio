# scripts/visualizaciones.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def plot_top_operadores_missed_calls(operator_perf):
    top_missed = operator_perf.sort_values(
        by='missed_calls', ascending=False).head(15)
    plt.figure(figsize=(10, 6))
    sns.barplot(data=top_missed, x='missed_calls',
                y='operator_id', palette='Reds_r')
    plt.title('Top 15 operadores con más llamadas perdidas')
    plt.xlabel('Llamadas perdidas')
    plt.ylabel('ID del operador')
    plt.grid(axis='x', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()


def plot_top_operadores_missed_calls_real(operator_perf):
    operadores_real = operator_perf[
        operator_perf['operator_id'].notna() &
        (~operator_perf['operator_id'].isin(['nan', '<NA>']))
    ]
    top_missed_real = operadores_real.sort_values(
        by='missed_calls', ascending=False).head(20)
    plt.figure(figsize=(10, 6))
    sns.barplot(data=top_missed_real, x='missed_calls',
                y='operator_id', palette='Reds_r')
    plt.title('Top 15 operadores con más llamadas perdidas (excluyendo NA)')
    plt.xlabel('Llamadas perdidas')
    plt.ylabel('ID del operador')
    plt.grid(axis='x', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()


def plot_wait_time_top_operadores(df_calls_no_outliers):
    top_operators = df_calls_no_outliers['operator_id'].value_counts().head(
        15).index
    df_top_wait = df_calls_no_outliers[df_calls_no_outliers['operator_id'].isin(
        top_operators)]
    plt.figure(figsize=(12, 6))
    sns.boxplot(data=df_top_wait, x='operator_id',
                y='wait_time', palette='coolwarm')
    plt.title(
        'Distribución de tiempos de espera por operador (Top 15 por volumen de llamadas)')
    plt.xlabel('ID del operador')
    plt.ylabel('Tiempo de espera (segundos)')
    plt.xticks(rotation=45)
    plt.grid(True, axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()


def plot_matriz_correlacion(operator_perf):
    cols_corr = [
        'total_calls', 'total_incoming', 'total_outgoing',
        'missed_calls', 'missed_rate', 'avg_wait_time',
        'avg_call_duration', 'criterios_cumplidos'
    ]
    corr_matrix = operator_perf[cols_corr].corr()
    plt.figure(figsize=(10, 8))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f",
                linewidths=0.5, square=True)
    plt.title('Matriz de correlación entre variables clave de desempeño')
    plt.tight_layout()
    plt.show()


def plot_hist_llamadas_salientes(operator_perf):
    plt.figure(figsize=(10, 6))
    plt.hist(operator_perf['total_outgoing'], bins=30,
             color='skyblue', edgecolor='black')
    plt.title('Distribución de llamadas salientes por operador')
    plt.xlabel('Cantidad de llamadas salientes')
    plt.ylabel('Número de operadores')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()


def mostrar_ranking_ineficientes(operator_perf):
    ranking_final = operator_perf.sort_values(
        by=['criterios_cumplidos', 'missed_rate', 'avg_wait_time'],
        ascending=False
    )
    ranking_cols = [
        'operator_id', 'criterios_cumplidos', 'missed_rate', 'avg_wait_time',
        'total_calls', 'total_incoming', 'total_outgoing',
        'ineficiente_missed', 'ineficiente_wait', 'ineficiente_outgoing'
    ]
    return ranking_final[ranking_cols].head(20)


def resumen_por_tarifa(operator_perf):
    tabla_tarifas = operator_perf.groupby('tariff_plan').agg(
        operadores_totales=('operator_id', 'nunique'),
        ineficientes=('es_ineficiente', 'sum'),
        prop_ineficientes=('es_ineficiente', 'mean'),
        missed_rate_promedio=('missed_rate', 'mean'),
        wait_time_promedio=('avg_wait_time', 'mean'),
        criterios_promedio=('criterios_cumplidos', 'mean')
    ).reset_index()
    return tabla_tarifas.sort_values(by='prop_ineficientes', ascending=False)
