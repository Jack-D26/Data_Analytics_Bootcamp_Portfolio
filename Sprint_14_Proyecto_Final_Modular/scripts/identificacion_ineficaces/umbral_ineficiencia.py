
import pandas as pd


def calcular_umbral_ineficiencia(df):
    """
    Calcula los umbrales de ineficiencia y agrega columnas booleanas
    según si el operador incumple los criterios establecidos.
    """
    # Umbrales
    missed_rate_threshold = df['missed_rate'].quantile(0.75)
    wait_time_threshold = df['avg_wait_time'].quantile(0.75)
    outgoing_calls_threshold = df['total_outgoing'].quantile(0.25)

    # Columnas booleanas de ineficiencia
    df['ineficiente_missed'] = df['missed_rate'] > missed_rate_threshold
    df['ineficiente_wait'] = df['avg_wait_time'] > wait_time_threshold
    df['ineficiente_outgoing'] = df['total_outgoing'] < outgoing_calls_threshold

    return df, missed_rate_threshold, wait_time_threshold, outgoing_calls_threshold


def etiquetar_ineficiencia(df, umbrales):
    df['ineficiente_missed'] = df['missed_rate'] > umbrales['missed_rate']
    df['ineficiente_wait'] = df['avg_wait_time'] > umbrales['avg_wait_time']
    df['ineficiente_outgoing'] = df['total_outgoing'] < umbrales['total_outgoing']

    df['es_ineficiente'] = (
        df['ineficiente_missed'] |
        df['ineficiente_wait'] |
        df['ineficiente_outgoing']
    )

    df['criterios_cumplidos'] = df[
        ['ineficiente_missed', 'ineficiente_wait', 'ineficiente_outgoing']
    ].sum(axis=1)

    return df
