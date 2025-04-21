import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


def plot_ineficientes_por_criterios(df):
    plt.figure(figsize=(7, 4))
    sns.countplot(data=df[df['es_ineficiente']],
                  x='criterios_cumplidos', palette='Reds')
    plt.title("Operadores ineficientes según cantidad de criterios fallidos")
    plt.xlabel("Número de criterios de ineficiencia cumplidos")
    plt.ylabel("Cantidad de operadores")
    plt.tight_layout()
    plt.show()


def plot_ineficiencia_por_plan(df):
    plt.figure(figsize=(6, 4))
    sns.countplot(data=df[df['es_ineficiente']],
                  x='tariff_plan', palette='coolwarm')
    plt.title("Operadores ineficientes por plan tarifario")
    plt.xlabel("Plan tarifario")
    plt.ylabel("Cantidad de operadores ineficientes")
    plt.tight_layout()
    plt.show()


def plot_torta_ineficiencia(df):
    labels = ['Ineficientes', 'Eficientes']
    sizes = [
        df['es_ineficiente'].sum(),
        df.shape[0] - df['es_ineficiente'].sum()
    ]
    plt.figure(figsize=(5, 5))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%',
            colors=['#f94144', '#90be6d'], startangle=140)
    plt.axis('equal')
    plt.title("Proporción de operadores ineficientes")
    plt.tight_layout()
    plt.show()


def plot_hist_total_llamadas(df):
    plt.figure(figsize=(10, 6))
    plt.hist(df['total_calls'], bins=30,
             color='mediumslateblue', edgecolor='black')
    plt.title("Distribución de llamadas totales por operador")
    plt.xlabel("Total de llamadas")
    plt.ylabel("Número de operadores")
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()


def plot_criterios_mas_frecuentes(df):
    criterios = ['ineficiente_missed',
                 'ineficiente_wait', 'ineficiente_outgoing']
    conteo = df[criterios].sum().sort_values(ascending=False).reset_index()
    conteo.columns = ['criterio', 'cantidad']

    nombres_legibles = {
        'ineficiente_missed': 'Alta tasa de llamadas perdidas',
        'ineficiente_wait': 'Largo tiempo de espera',
        'ineficiente_outgoing': 'Pocas llamadas salientes'
    }
    conteo['criterio'] = conteo['criterio'].map(nombres_legibles)

    plt.figure(figsize=(8, 4))
    sns.barplot(data=conteo, x='criterio', y='cantidad', palette='flare')
    plt.title("Criterios de ineficiencia más frecuentes")
    plt.xlabel("Criterio de ineficiencia")
    plt.ylabel("Cantidad de operadores")
    plt.xticks(rotation=20)
    plt.tight_layout()
    plt.show()
