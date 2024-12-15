import streamlit as st
from src.data.cleaners import preparar_datos
from src.data.transformers import (
    producto_mas_ingresos,
    ranking_problemas,
    top_10_ejecutivos,
    porcentaje_estados,
    promedio_vida_util,
    producto_menor_vida_util,
    casos_por_mes
)
import matplotlib.pyplot as plt
import seaborn as sns

# Configuración global de estilo de las gráficas
sns.set(style="whitegrid")

# Ruta del archivo de datos
RUTA_ARCHIVO = "data_file/DATA_ANALIZAR.csv"

# Cargar y limpiar los datos
data = preparar_datos(RUTA_ARCHIVO)

# Función para mostrar gráficos en Streamlit
def mostrar_grafico(funcion_transformacion, titulo, **kwargs):
    datos = funcion_transformacion(data, **kwargs)
    plt.figure(figsize=(10, 6))
    
    if titulo == 'Producto con más ingresos registrados':
        sns.barplot(x=datos['PRODUCTO'], y=datos['Total ingresos'], color='green')
    elif titulo == 'Ranking de problemas más frecuentes':
        sns.barplot(x='Total casos', y='Problema', data=datos, color='red')
    elif titulo == 'Top 10 ejecutivos con más casos atendidos':
        sns.barplot(x='Total casos', y='Ejecutivo', data=datos, color='blue')
    elif titulo == 'Porcentaje de estados (abiertos/cerrados)':
        # Asegúrate de que los datos estén ordenados y preparados correctamente
        ax = sns.barplot(x='Estado', y='Porcentaje', data=datos, hue='Estado', palette='coolwarm', legend=False)
        # Agregar anotaciones a las barras
        for p in ax.patches:
            ax.annotate(f'{p.get_height():.2f}%', 
                        (p.get_x() + p.get_width() / 2., p.get_height()), 
                        ha='center', va='center', 
                        fontsize=12, color='black', 
                        xytext=(0, 10), textcoords='offset points')
    elif titulo == 'Promedio de vida útil del producto':
        sns.barplot(x=['Promedio de vida útil'], y=[datos], color='orange')
    elif titulo == 'Producto con menor vida útil':
        sns.barplot(x='PRODUCTO', y='TIEMPO DE USO ABSOLUTO', data=datos, color='cyan')
    elif titulo == 'Casos por mes':
        sns.barplot(x='Mes', y='Total casos', data=datos, palette='muted')
    
    # Mejorar la presentación
    plt.title(titulo, fontsize=16, fontweight='bold')
    plt.xlabel('Categoría', fontsize=14)
    plt.ylabel('Valor', fontsize=14)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    
    # Mostrar el gráfico en Streamlit
    st.pyplot(plt)
    plt.close()

# Configuración de la aplicación Streamlit
st.title("Dashboard de Análisis de Datos")
st.sidebar.title("Opciones de Visualización")

grafico_seleccionado = st.sidebar.selectbox(
    "Selecciona el gráfico a mostrar:",
    [
        "Producto con más ingresos registrados",
        "Ranking de problemas más frecuentes",
        "Top 10 ejecutivos con más casos atendidos",
        "Porcentaje de estados (abiertos/cerrados)",
        "Promedio de vida útil del producto",
        "Producto con menor vida útil",
        "Casos por mes",
    ]
)

# Mostrar el gráfico correspondiente al seleccionar la opción
if grafico_seleccionado == "Producto con más ingresos registrados":
    mostrar_grafico(producto_mas_ingresos, grafico_seleccionado)
elif grafico_seleccionado == "Ranking de problemas más frecuentes":
    mostrar_grafico(ranking_problemas, grafico_seleccionado)
elif grafico_seleccionado == "Top 10 ejecutivos con más casos atendidos":
    mostrar_grafico(top_10_ejecutivos, grafico_seleccionado)
elif grafico_seleccionado == "Porcentaje de estados (abiertos/cerrados)":
    mostrar_grafico(porcentaje_estados, grafico_seleccionado)
elif grafico_seleccionado == "Promedio de vida útil del producto":
    mostrar_grafico(promedio_vida_util, grafico_seleccionado)
elif grafico_seleccionado == "Producto con menor vida útil":
    mostrar_grafico(producto_menor_vida_util, grafico_seleccionado)
elif grafico_seleccionado == "Casos por mes":
    mostrar_grafico(casos_por_mes, grafico_seleccionado)
