import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import pearsonr, kruskal, mannwhitneyu


def prueba_correlacion_entrantes_missed(df):
    corr, p_value = pearsonr(df['total_incoming'], df['missed_rate'])
    print(f"Coeficiente de correlación de Pearson: {corr:.4f}")
    print(f"Valor p: {p_value:.4f}")
    if p_value < 0.05:
        print("Resultado significativo: Existe una correlación estadísticamente significativa.")
    else:
        print("No significativo: No se puede afirmar que haya una correlación estadísticamente significativa.")


def prueba_correlacion_espera_missed(df_calls, operator_perf):
    wait_time_mean = df_calls.groupby(
        'operator_id')['wait_time'].mean().reset_index()
    wait_time_mean.rename(
        columns={'wait_time': 'wait_time_mean'}, inplace=True)
    df_corr = operator_perf.merge(wait_time_mean, on='operator_id', how='left')
    df_corr = df_corr[['wait_time_mean', 'missed_rate']].dropna()
    corr, p_value = pearsonr(df_corr['wait_time_mean'], df_corr['missed_rate'])
    print(f"Coeficiente de correlación de Pearson: {corr:.4f}")
    print(f"Valor p: {p_value:.4f}")
    if p_value < 0.05:
        print("Resultado significativo: Existe una correlación estadísticamente significativa.")
    else:
        print("No significativo: No se puede afirmar que haya una correlación estadísticamente significativa.")


def prueba_planes_tarifarios(df_calls, df_clients):
    df_merged = df_calls.merge(
        df_clients[['user_id', 'tariff_plan']], on='user_id', how='left')
    plan_perf = df_merged.groupby(['operator_id', 'tariff_plan']).agg(
        missed_calls=('is_missed_call', 'sum'),
        total_calls=('is_missed_call', 'count'),
        wait_time_mean=('wait_time', 'mean')
    ).reset_index()
    plan_perf['missed_rate'] = plan_perf['missed_calls'] / \
        plan_perf['total_calls']

    plt.figure(figsize=(8, 5))
    sns.boxplot(data=plan_perf, x='tariff_plan', y='missed_rate')
    plt.title("Tasa de llamadas perdidas por plan tarifario")
    plt.ylabel("Missed Rate")
    plt.xlabel("Plan Tarifario")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    group_A = plan_perf[plan_perf['tariff_plan'] == 'A']['missed_rate']
    group_B = plan_perf[plan_perf['tariff_plan'] == 'B']['missed_rate']
    group_C = plan_perf[plan_perf['tariff_plan'] == 'C']['missed_rate']
    stat, p_value = kruskal(group_A, group_B, group_C)
    print(f"Estadístico H de Kruskal-Wallis: {stat:.4f}")
    print(f"Valor p: {p_value:.4f}")
    if p_value < 0.05:
        print("Resultado significativo: Al menos un plan tarifario difiere en la tasa de llamadas perdidas.")
    else:
        print("No significativo: No hay diferencias significativas entre los planes tarifarios.")


def prueba_antiguedad_eficiencia(df_calls, df_clients, operator_perf):
    df_antiguedad = df_calls.merge(
        df_clients[['user_id', 'date_start']], on='user_id', how='left')
    df_antiguedad['antiguedad_dias'] = (pd.to_datetime(
        '2025-04-01') - pd.to_datetime(df_antiguedad['date_start'])).dt.days
    antiguedad_op = df_antiguedad.groupby(
        'operator_id')['antiguedad_dias'].mean().reset_index()
    antiguedad_op.rename(
        columns={'antiguedad_dias': 'avg_antiguedad_dias'}, inplace=True)
    operator_perf = operator_perf.merge(
        antiguedad_op, on='operator_id', how='left')
    df_corr = operator_perf[['avg_antiguedad_dias', 'missed_rate']].dropna()
    corr, p_value = pearsonr(
        df_corr['avg_antiguedad_dias'], df_corr['missed_rate'])
    print(f"Coeficiente de Pearson: {corr:.4f}")
    print(f"Valor p: {p_value:.4f}")
    if p_value < 0.05:
        print("Resultado significativo: La antigüedad del cliente tiene impacto en la eficiencia del operador.")
    else:
        print(
            "No significativo: No hay relación significativa entre antigüedad y desempeño.")


def prueba_comparacion_operadores(operator_perf):
    ineficientes = operator_perf[operator_perf['es_ineficiente'] == True]
    eficientes = operator_perf[operator_perf['es_ineficiente'] == False]

    stat_missed, p_missed = mannwhitneyu(
        ineficientes['missed_rate'], eficientes['missed_rate'], alternative='two-sided')
    stat_wait, p_wait = mannwhitneyu(
        ineficientes['avg_wait_time'], eficientes['avg_wait_time'], alternative='two-sided')

    print(
        f"[missed_rate] Estadístico U: {stat_missed:.4f}, p-value: {p_missed:.4f}")
    print(
        f"[avg_wait_time] Estadístico U: {stat_wait:.4f}, p-value: {p_wait:.4f}")

    if p_missed < 0.05:
        print("Diferencia significativa en tasas de llamadas perdidas entre eficientes e ineficientes.")
    if p_wait < 0.05:
        print(
            "Diferencia significativa en tiempos de espera entre eficientes e ineficientes.")
