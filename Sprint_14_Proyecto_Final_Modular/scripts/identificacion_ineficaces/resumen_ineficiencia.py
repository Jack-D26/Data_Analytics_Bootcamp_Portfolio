import pandas as pd


def calcular_resumen_ineficiencia(df):
    total = df.shape[0]
    ineficientes = df['es_ineficiente'].sum()
    proporcion = round(ineficientes / total, 4)
    return {
        'total_operadores': total,
        'ineficientes': ineficientes,
        'proporcion_ineficientes': proporcion
    }


def resumen_por_plan(df):
    resumen = df.groupby('tariff_plan').agg(
        total_operadores=('operator_id', 'count'),
        ineficientes=('es_ineficiente', 'sum')
    ).reset_index()

    resumen['proporcion_ineficientes'] = (
        resumen['ineficientes'] / resumen['total_operadores']).round(3)
    return resumen


def criterios_por_plan(df):
    criterios = ['ineficiente_missed',
                 'ineficiente_wait', 'ineficiente_outgoing']
    resumen = df[df['es_ineficiente']].groupby(
        'tariff_plan')[criterios].sum().reset_index()
    return resumen
