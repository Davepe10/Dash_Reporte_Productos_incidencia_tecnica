import streamlit as st
from src.visualizations.plots import (
    plot_producto_mas_ingresos,
    plot_ranking_problemas,
    plot_casos_por_mes,
    plot_top_10_ejecutivos,
    plot_porcentaje_estados,
    plot_promedio_vida_util,
    plot_producto_menor_vida_util
)
from src.data.cleaners import preparar_datos

# Ruta del archivo de datos
RUTA_ARCHIVO = "data_file/DATA_ANALIZAR.csv"

# Cargar y limpiar los datos
data = preparar_datos(RUTA_ARCHIVO)

# Configuración inicial
st.set_page_config(
    page_title="Dashboard de Análisis de Datos",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilo de letra y tamaño del título
theme_css = """
<style>
h1 {
    font-size: 24px;
    color: #4C4C4C;
}
body {
    font-family: 'Arial', sans-serif;
    color: #333;
}
</style>
"""
st.markdown(theme_css, unsafe_allow_html=True)

# Título y descripción
st.title("Dashboard de Análisis de Productos e Incidencias")
st.markdown(
    """
    Este dashboard presenta un análisis interactivo de productos reportados por incidencias.
    Puedes explorar los gráficos principales o seleccionar uno para un análisis detallado.
    """
)

# Panel inicial: Mostrar todos los gráficos en dos columnas
st.header("Visión General")
col1, col2 = st.columns([1, 1])  # Cambiar la distribución de las columnas (más espacio para la primera columna)

# Gráfico: Producto con más incidencias
with col1:
    fig1 = plot_producto_mas_ingresos(data)
    st.plotly_chart(fig1, use_container_width=True)
    st.write("**Análisis:** Este producto tiene el mayor número de incidencias reportadas, lo que indica que es el que presenta más fallas.")
    st.write("**Recomendación:** Mejorar la calidad de este producto, reforzando controles de calidad y revisando posibles fallas recurrentes.")

# Gráfico: Casos por Mes
with col2:
    fig3 = plot_casos_por_mes(data)
    st.plotly_chart(fig3, use_container_width=True)
    st.write("**Análisis:** La cantidad de incidencias varía a lo largo del año, lo que podría estar relacionado con factores estacionales o picos en fallas.")
    st.write("**Recomendación:** Aumentar los recursos de atención al cliente y de soporte durante los meses con más incidencias para mejorar el tiempo de respuesta.")

# Agregar más gráficos
col3, col4 = st.columns(2)

# Gráfico: Top 10 Ejecutivos
with col3:
    fig4 = plot_top_10_ejecutivos(data)
    st.plotly_chart(fig4, use_container_width=True)
    st.write("**Análisis:** Los ejecutivos con más incidencias reportadas podrían tener un enfoque más proactivo o estar involucrados en casos complejos.")
    st.write("**Recomendación:** Capacitar a otros ejecutivos basándose en las mejores prácticas de los más efectivos para mejorar la resolución de incidencias.")

# Gráfico: Porcentaje de Estados (Abierto/Cerrado)
with col3:
    fig5 = plot_porcentaje_estados(data)
    st.plotly_chart(fig5, use_container_width=True)
    st.write("**Análisis:** La proporción de incidencias abiertas frente a cerradas puede indicar la eficiencia en la resolución de problemas.")
    st.write("**Recomendación:** Acelerar el cierre de incidencias abiertas para mejorar la eficiencia del proceso y la satisfacción del cliente.")

# Gráfico: Promedio de Vida Útil
with col4:
    fig6 = plot_promedio_vida_util(data)
    st.plotly_chart(fig6, use_container_width=True)
    st.write("**Análisis:** El promedio de vida útil de los productos puede reflejar su durabilidad y la calidad general del diseño o materiales.")
    st.write("**Recomendación:** Mejorar el diseño o la selección de materiales para aumentar la vida útil y reducir las incidencias relacionadas con fallas tempranas.")

# Gráfico: Producto con Menor Vida Útil
with col4:
    fig7 = plot_producto_menor_vida_util(data)
    st.plotly_chart(fig7, use_container_width=True)
    st.write("**Análisis:** Este producto presenta una vida útil inferior al promedio, lo que puede generar un mayor número de incidencias o quejas.")
    st.write("**Recomendación:** Mejorar los procesos de fabricación o rediseñar el producto para extender su vida útil y reducir las incidencias asociadas.")

# Agregar el gráfico de Ranking de Problemas que ocupe todo el ancho de la página
st.header("Ranking de Problemas")
fig2 = plot_ranking_problemas(data)
st.plotly_chart(fig2, use_container_width=True)
st.write("**Análisis:** Los problemas más comunes están relacionados con fallas técnicas o de funcionamiento de los productos.")
st.write("**Recomendación:** Centrar los esfuerzos en solucionar los problemas más frecuentes para mejorar la satisfacción del cliente y reducir las incidencias.")

# Asegurar diseño responsive para móviles
st.markdown(
    """
    <style>
    @media (max-width: 768px) {
        .css-1d391kg, .css-18e3th9 {
            flex-direction: column;
        }
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Selección interactiva para análisis detallado
st.header("Análisis Detallado")
opcion = st.selectbox(
    "Selecciona un gráfico para explorar:",
    ("Producto Más Reportado por Fallas", "Ranking de Problemas por Producto", "Top 10 Ejecutivos con Más Incidencias Reportadas",
     "Porcentaje de Estados de Incidencias", "Promedio de Vida Útil", "Producto con Menor Vida Útil", "Incidencias Reportadas por Mes")
)

# Lógica para mostrar el gráfico seleccionado en detalle (sin análisis ni recomendación)
if opcion == "Producto Más Reportado por Fallas":
    st.subheader("Producto Más Reportado por Fallas")
    fig1 = plot_producto_mas_ingresos(data)
    st.plotly_chart(fig1)

elif opcion == "Ranking de Problemas por Producto":
    st.subheader("Ranking de Problemas por Producto")
    fig2 = plot_ranking_problemas(data)
    st.plotly_chart(fig2)

elif opcion == "Incidencias Reportadas por Mes":
    st.subheader("Incidencias Reportadas por Mes")
    fig3 = plot_casos_por_mes(data)
    st.plotly_chart(fig3)

elif opcion == "Top 10 Ejecutivos con Más Incidencias Reportadas":
    st.subheader("Top 10 Ejecutivos con Más Incidencias Reportadas")
    fig4 = plot_top_10_ejecutivos(data)
    st.plotly_chart(fig4)

elif opcion == "Porcentaje de Estados de Incidencias":
    st.subheader("Porcentaje de Estados de Incidencias (Abierto/Cerrado)")
    fig5 = plot_porcentaje_estados(data)
    st.plotly_chart(fig5)

elif opcion == "Promedio de Vida Útil":
    st.subheader("Promedio de Vida Útil")
    fig6 = plot_promedio_vida_util(data)
    st.plotly_chart(fig6)

elif opcion == "Producto con Menor Vida Útil":
    st.subheader("Producto con Menor Vida Útil")
    fig7 = plot_producto_menor_vida_util(data)
    st.plotly_chart(fig7)
