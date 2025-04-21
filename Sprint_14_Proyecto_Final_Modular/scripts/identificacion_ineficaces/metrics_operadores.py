import pandas as pd


def calcular_metricas_por_operador(df):
    """
    Agrupa y calcula métricas clave de desempeño por operador.
    """
    operator_perf = df.groupby('operator_id').agg(
        total_calls=('operator_id', 'size'),
        total_incoming=('direction', lambda x: (x == 'in').sum()),
        total_outgoing=('direction', lambda x: (x == 'out').sum()),
        missed_calls=('missed_call', 'sum'),
        missed_rate=('missed_call', 'mean'),
        avg_wait_time=('wait_time', 'mean'),
        avg_call_duration=('call_duration', 'mean')
    ).reset_index()

    return operator_perf


def agregar_plan_a_operadores(df_operators, df_clients):
    """
    Hace merge del dataframe de operadores con el de clientes para añadir el plan tarifario.
    """
    df_merged = df_operators.merge(
        df_clients[['user_id', 'tariff_plan']], on='user_id', how='left')
    return df_merged


def calcular_metricas_con_plan(df):
    """
    Agrupa nuevamente por operador incluyendo el plan tarifario.
    """
    operator_perf = df.groupby('operator_id').agg(
        total_calls=('operator_id', 'size'),
        total_incoming=('direction', lambda x: (x == 'in').sum()),
        total_outgoing=('direction', lambda x: (x == 'out').sum()),
        missed_calls=('missed_call', 'sum'),
        missed_rate=('missed_call', 'mean'),
        avg_wait_time=('wait_time', 'mean'),
        avg_call_duration=('call_duration', 'mean'),
        tariff_plan=('tariff_plan', 'first')
    ).reset_index()

    return operator_perf
