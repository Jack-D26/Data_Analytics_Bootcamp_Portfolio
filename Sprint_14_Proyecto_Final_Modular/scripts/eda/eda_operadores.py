import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def calcular_metricas_operadores(df):
    df_grouped = df.groupby('operator_id').agg({
        'direction': lambda x: (x == 'in').sum(),
        'internal': lambda x: (x == True).sum(),
        'is_missed_call': 'mean',
        'call_duration': 'mean',
        'wait_time': 'mean'
    }).rename(columns={
        'direction': 'llamadas_entrantes',
        'internal': 'llamadas_internas',
        'is_missed_call': 'promedio_llamadas_perdidas',
        'call_duration': 'duracion_promedio',
        'wait_time': 'espera_promedio'
    })
    df_grouped['llamadas_salientes'] = df.groupby(
        'operator_id').size() - df_grouped['llamadas_entrantes']
    return df_grouped.reset_index().sort_values(by='operator_id')


def plot_top_operadores(df_operador_llamadas):
    df_operador_llamadas['total_llamadas'] = df_operador_llamadas[[
        'llamadas_entrantes', 'llamadas_salientes', 'llamadas_internas']].sum(axis=1)
    top_operadores = df_operador_llamadas.nlargest(15, 'total_llamadas')
    df_long = top_operadores.melt(
        id_vars='operator_id',
        value_vars=['llamadas_entrantes',
                    'llamadas_salientes', 'llamadas_internas'],
        var_name='tipo_llamada',
        value_name='cantidad'
    )
    plt.figure(figsize=(12, 6))
    sns.barplot(data=df_long, x='operator_id',
                y='cantidad', hue='tipo_llamada')
    plt.title('Distribución de llamadas por tipo y operador (Top 15)')
    plt.xlabel('ID Operador')
    plt.ylabel('Cantidad de llamadas')
    plt.xticks(rotation=45)
    plt.legend(title='Tipo de llamada')
    plt.tight_layout()
    plt.show()
