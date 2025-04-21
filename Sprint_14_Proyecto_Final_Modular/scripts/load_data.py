# scripts/load_data.py

import pandas as pd


def load_clients_data():
    """
    Carga el dataset de clientes desde URL.
    Retorna un DataFrame.
    """
    url_clients = "https://practicum-content.s3.us-west-1.amazonaws.com/datasets/telecom_clients_us.csv"
    return pd.read_csv(url_clients)


def load_calls_data():
    """
    Carga el dataset de llamadas desde URL.
    Retorna un DataFrame.
    """
    url_calls = "https://practicum-content.s3.us-west-1.amazonaws.com/datasets/telecom_dataset_us.csv"
    return pd.read_csv(url_calls)


if __name__ == "__main__":
    df_clients = load_clients_data()
    df_calls = load_calls_data()

    print("Clientes:")
    print(df_clients.head())
    print("\nLlamadas:")
    print(df_calls.head())
