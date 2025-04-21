import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def crear_columna_llamada_perdida(df):
    df['missed_call'] = (df['wait_time'] > 0) & (df['call_duration'] == 0)
    return df


def binarizar_wait_time(df):
    bins = [0, 10, 20, 30, 60, 120, 180, 300]
    labels = ['0-10s', '11-20s', '21-30s',
              '31-60s', '61-120s', '121-180s', '181-300s']
    df['wait_bin'] = pd.cut(df['wait_time'], bins=bins,
                            labels=labels, right=False)
    return df


def resumen_llamadas_perdidas(df):
    missed_summary = df.groupby('wait_bin')['missed_call'].agg(
        ['count', 'sum', 'mean']).reset_index()
    missed_summary.rename(columns={'count': 'total_llamadas',
                          'sum': 'llamadas_perdidas', 'mean': 'proporcion_perdidas'}, inplace=True)
    return missed_summary


def plot_llamadas_perdidas(df):
    plt.figure(figsize=(10, 5))
    sns.barplot(data=df, x='wait_bin', y='proporcion_perdidas', color='salmon')
    plt.title("Proporción de llamadas perdidas por rango de tiempo de espera")
    plt.xlabel("Rango de tiempo de espera")
    plt.ylabel("Proporción de llamadas perdidas")
    plt.ylim(0, 1)
    plt.tight_layout()
    plt.show()
