import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def resumen_estadistico_tiempos(df):
    return df[['call_duration', 'wait_time']].describe()


def plot_hist_tiempos(df):
    fig, axs = plt.subplots(1, 2, figsize=(16, 5))
    sns.histplot(df['call_duration'], bins=50, kde=True, ax=axs[0])
    axs[0].set_title("Distribución de duración de llamadas (sin outliers)")
    axs[0].set_xlabel("Duración (segundos)")
    sns.histplot(df['wait_time'], bins=50, kde=True, ax=axs[1], color='orange')
    axs[1].set_title("Distribución del tiempo de espera (sin outliers)")
    axs[1].set_xlabel("Tiempo de espera (segundos)")
    plt.tight_layout()
    plt.show()


def filtrar_outliers_wait_time(df):
    Q1 = df['wait_time'].quantile(0.25)
    Q3 = df['wait_time'].quantile(0.75)
    IQR = Q3 - Q1
    li, ls = Q1 - 1.5 * IQR, Q3 + 1.5 * IQR
    return df[(df['wait_time'] >= li) & (df['wait_time'] <= ls)].copy()
