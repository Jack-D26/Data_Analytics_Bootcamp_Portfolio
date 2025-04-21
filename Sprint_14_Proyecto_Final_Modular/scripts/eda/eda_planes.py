import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def promedio_llamadas_por_plan(df):
    llamadas_por_plan = df.groupby(['operator_id', 'tariff_plan']).agg({
        'direction': [
            lambda x: (x == 'in').sum(),
            lambda x: (x == 'out').sum(),
            lambda x: (x == 'internal').sum()
        ]
    }).reset_index()
    llamadas_por_plan.columns = ['operator_id', 'tariff_plan',
                                 'llamadas_entrantes', 'llamadas_salientes', 'llamadas_internas']
    promedios = llamadas_por_plan.groupby('tariff_plan')[
        ['llamadas_entrantes', 'llamadas_salientes', 'llamadas_internas']].mean().reset_index()
    return promedios


def plot_promedio_llamadas_por_plan(df):
    df_melted = df.melt(id_vars='tariff_plan',
                        var_name='tipo_llamada', value_name='promedio_llamadas')
    plt.figure(figsize=(10, 6))
    sns.barplot(data=df_melted, x='tariff_plan',
                y='promedio_llamadas', hue='tipo_llamada')
    plt.title("Promedio de llamadas por tipo y plan tarifario (por operador)")
    plt.xlabel("Plan Tarifario")
    plt.ylabel("Promedio de llamadas por operador")
    plt.legend(title="Tipo de llamada")
    plt.tight_layout()
    plt.show()
