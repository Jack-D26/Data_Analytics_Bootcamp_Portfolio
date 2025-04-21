# scripts/preprocessing.py

import pandas as pd


def convertir_tipos(df_clients, df_calls):
    """
    Convierte tipos de datos en ambos DataFrames.
    """
    df_clients['user_id'] = df_clients['user_id'].astype(str)
    df_calls['user_id'] = df_calls['user_id'].astype(str)
    df_calls['operator_id'] = df_calls['operator_id'].astype(
        'Int64').astype(str)
    df_clients['date_start'] = pd.to_datetime(df_clients['date_start'])
    df_calls['date'] = pd.to_datetime(df_calls['date'])
    df_calls['call_date'] = pd.to_datetime(df_calls['date'].dt.date)
    df_calls['call_time'] = pd.to_datetime(
        df_calls['date'].dt.strftime('%H:%M:%S'), format='%H:%M:%S')
    return df_clients, df_calls


def revisar_nulos(df, nombre_df):
    """
    Imprime resumen de nulos y porcentaje.
    """
    print(f"\nNulos en {nombre_df}:")
    nulos = df.isnull().sum()
    porcentaje = (nulos / len(df)) * 100
    resumen = pd.DataFrame({'Nulos': nulos, 'Porcentaje': porcentaje.round(2)})
    print(resumen)


def revisar_duplicados(df, nombre_df):
    """
    Imprime cantidad de duplicados exactos.
    """
    duplicados = df.duplicated().sum()
    print(f"{nombre_df} tiene {duplicados} registros duplicados.")


def limpiar_nulos_y_duplicados(df_calls):
    """
    Aplica limpieza de nulos y duplicados sobre df_calls.
    """
    # Reemplazo explícito de strings 'nan', '<NA>' por pd.NA
    df_calls['operator_id'] = df_calls['operator_id'].replace(
        ['nan', '<NA>'], pd.NA)

    # Eliminar registros con 'internal' nulo
    df_calls = df_calls[df_calls['internal'].notna()]

    # Eliminar duplicados exactos
    df_calls = df_calls.drop_duplicates()

    return df_calls
