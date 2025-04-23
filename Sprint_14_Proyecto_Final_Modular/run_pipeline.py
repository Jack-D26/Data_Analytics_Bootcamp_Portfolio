# run_pipeline.py

import os

# run_pipeline.py

# === Load & Clean ===
from scripts.load_data import load_clients_data, load_calls_data
from scripts.preprocessing import (
    convertir_tipos, revisar_nulos, revisar_duplicados, limpiar_nulos_y_duplicados
)

# === EDA & Feature Engineering ===
from scripts.eda.eda_llamadas_perdidas import crear_columna_llamada_perdida, binarizar_wait_time
from scripts.eda.eda_tiempos import filtrar_outliers_wait_time
from scripts.identificacion_ineficaces.metrics_operadores import calcular_metricas_con_plan

# === Inefficiency Analysis ===
from scripts.identificacion_ineficaces.umbral_ineficiencia import calcular_umbral_ineficiencia, etiquetar_ineficiencia
from scripts.identificacion_ineficaces.resumen_ineficiencia import calcular_resumen_ineficiencia
from scripts.identificacion_ineficaces.ineficiencia_visuals import (
    plot_ineficientes_por_criterios,
    plot_ineficiencia_por_plan,
    plot_torta_ineficiencia,
    plot_hist_total_llamadas,
    plot_criterios_mas_frecuentes
)

# === Visualization & Hypothesis Testing ===
from scripts.visualizaciones import (
    plot_top_operadores_missed_calls_real,
    plot_wait_time_top_operadores,
    plot_matriz_correlacion,
    mostrar_ranking_ineficientes,
    resumen_por_tarifa
)
from scripts.pruebas_hipotesis import (
    prueba_correlacion_entrantes_missed,
    prueba_correlacion_espera_missed,
    prueba_planes_tarifarios,
    prueba_antiguedad_eficiencia,
    prueba_comparacion_operadores
)


def main():
    print("🚀 Iniciando pipeline de análisis CallMeMaybe...\n")

    # 1. Carga de datos
    df_clients = load_clients_data()
    df_calls = load_calls_data()

    # 2. Preprocesamiento
    df_clients, df_calls = convertir_tipos(df_clients, df_calls)
    revisar_nulos(df_clients, "Clientes")
    revisar_nulos(df_calls, "Llamadas")
    revisar_duplicados(df_clients, "Clientes")
    revisar_duplicados(df_calls, "Llamadas")
    df_calls = limpiar_nulos_y_duplicados(df_calls)

    # Fix call_duration and wait_time before EDA
    df_calls['call_duration'] = df_calls['call_duration'].fillna(0)
    df_calls['wait_time'] = (df_calls['calls_count']
                             * 60) - df_calls['call_duration']

    # 3. Ingeniería de características (EDA)
    df_calls = crear_columna_llamada_perdida(df_calls)
    df_calls = binarizar_wait_time(df_calls)
    df_calls['is_missed_call'] = df_calls['missed_call']
    df_calls_no_outliers = filtrar_outliers_wait_time(df_calls)

    # 4. Métricas por operador (con plan tarifario)
    df_calls = df_calls.merge(
        df_clients[['user_id', 'tariff_plan']], on='user_id', how='left')
    operator_perf = calcular_metricas_con_plan(df_calls)

    # 5. Identificación de operadores ineficientes
    operator_perf, missed_thr, wait_thr, outgoing_thr = calcular_umbral_ineficiencia(
        operator_perf)
    umbrales = {
        'missed_rate': missed_thr,
        'avg_wait_time': wait_thr,
        'total_outgoing': outgoing_thr
    }
    operator_perf = etiquetar_ineficiencia(operator_perf, umbrales)

    # 6. Visualizaciones sobre ineficiencia
    plot_ineficientes_por_criterios(operator_perf)
    plot_ineficiencia_por_plan(operator_perf)
    plot_torta_ineficiencia(operator_perf)
    plot_hist_total_llamadas(operator_perf)
    plot_criterios_mas_frecuentes(operator_perf)

    # 7. Reportes y tablas resumen
    print(mostrar_ranking_ineficientes(operator_perf))
    print(resumen_por_tarifa(operator_perf))

    # 8. Pruebas estadísticas
    prueba_correlacion_entrantes_missed(operator_perf)
    prueba_correlacion_espera_missed(df_calls_no_outliers, operator_perf)
    prueba_planes_tarifarios(df_calls_no_outliers, df_clients)
    prueba_antiguedad_eficiencia(
        df_calls_no_outliers, df_clients, operator_perf)
    prueba_comparacion_operadores(operator_perf)

    # 9. Resumen ejecutivo
    resumen = calcular_resumen_ineficiencia(operator_perf)
    print("📊 Resumen general de ineficiencia:", resumen)

    print("\n✅ Pipeline finalizado correctamente.")

    # === Save Report ===
    print("💾 Guardando reporte de resultados en docs/report.md...")
    report_path = "docs/report.md"
    with open(report_path, "w", encoding="utf-8") as f:
        f.write("# 📊 Reporte de Resultados: CallMeMaybe\n\n")

        f.write("## 🔹 Resumen General\n")
        f.write(f"- Total operadores: {resumen['total_operadores']}\n")
        f.write(f"- Ineficientes: {resumen['ineficientes']}\n")
        f.write(
            f"- Proporción ineficientes: {resumen['proporcion_ineficientes']:.2%}\n\n")

        f.write("## 🥇 Top 10 Operadores Ineficientes\n")
        top_inef = mostrar_ranking_ineficientes(operator_perf).head(10)
        f.write(top_inef.to_markdown(index=False))
        f.write("\n\n")

        f.write("## 📊 Desempeño por Plan Tarifario\n")
        resumen_planes = resumen_por_tarifa(operator_perf)
        f.write(resumen_planes.to_markdown(index=False))
        f.write("\n\n")

    print(f"📄 Reporte guardado en: {report_path}")


if __name__ == "__main__":
    main()
