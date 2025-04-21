import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def merge_outliers_with_clients(df_outliers, df_clients):
    return df_outliers.merge(df_clients, on='user_id', how='left')


def resumen_outliers_por_plan(df_merged):
    conteo = df_merged['tariff_plan'].value_counts().sort_index()
    proporcion = (conteo / len(df_merged) * 100).round(2)
    return pd.DataFrame({
        'Cantidad de Outliers': conteo,
        'Proporción (%)': proporcion
    })


def plot_outliers_por_plan(resumen):
    plt.figure(figsize=(6, 4))
    sns.barplot(x=resumen.index,
                y=resumen['Cantidad de Outliers'], palette='Set2')
    plt.title("Cantidad de llamadas con duración atípica por plan tarifario")
    plt.xlabel("Plan Tarifario")
    plt.ylabel("Cantidad de Outliers")
    plt.show()
