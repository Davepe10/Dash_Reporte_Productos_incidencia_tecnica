import matplotlib.pyplot as plt
import seaborn as sns
from src.data.transformers import (
    producto_mas_ingresos,
    ranking_problemas,
    top_10_ejecutivos,
    porcentaje_estados,
    promedio_vida_util,
    producto_menor_vida_util,
    casos_por_mes
)

# Configuración global de estilo de las gráficas
sns.set(style="whitegrid")

def graficar_producto_mas_ingresos(data):
    producto = producto_mas_ingresos(data)
    plt.figure(figsize=(8, 5))
    sns.barplot(x=producto['PRODUCTO'], y=producto['Total ingresos'], color='green')
    plt.title('Producto con más ingresos registrados')
    plt.xlabel('Producto')
    plt.ylabel('Total ingresos')
    plt.show()

def graficar_ranking_problemas(data):
    ranking = ranking_problemas(data)
    plt.figure(figsize=(10, 6))
    sns.barplot(x='Total casos', y='Problema', data=ranking, color='red')
    plt.title('Ranking de problemas más frecuentes')
    plt.xlabel('Total de casos')
    plt.ylabel('Problema')
    plt.show()

def graficar_top_10_ejecutivos(data):
    top_10 = top_10_ejecutivos(data)
    plt.figure(figsize=(10, 6))
    sns.barplot(x='Total casos', y='Ejecutivo', data=top_10, color='blue')
    plt.title('Top 10 ejecutivos con más casos atendidos')
    plt.xlabel('Total casos')
    plt.ylabel('Ejecutivo')
    plt.show()

def graficar_porcentaje_estados(data):
    estados = porcentaje_estados(data)
    plt.figure(figsize=(8, 5))
    sns.barplot(x='Estado', y='Porcentaje', data=estados, hue= 'Estado',palette='coolwarm', legend=False)
    plt.title('Porcentaje de estados (abiertos/cerrados)')
    plt.xlabel('Estado')
    plt.ylabel('Porcentaje')
    plt.show()

def graficar_promedio_vida_util(data):
    promedio = promedio_vida_util(data)
    plt.figure(figsize=(8, 5))
    sns.barplot(x=['Promedio de vida útil'], y=[promedio], color='orange')
    plt.title('Promedio de vida útil del producto')
    plt.ylabel('Días')
    plt.show()

def graficar_producto_menor_vida_util(data):
    producto_menor = producto_menor_vida_util(data)
    plt.figure(figsize=(8, 5))
    sns.barplot(x='PRODUCTO', y='TIEMPO DE USO ABSOLUTO', data=producto_menor, color='cyan')
    plt.title('Producto con menor vida útil')
    plt.xlabel('Producto')
    plt.ylabel('Vida útil (días)')
    plt.show()

def graficar_casos_por_mes(data):
    casos = casos_por_mes(data)
    plt.figure(figsize=(10, 6))
    sns.barplot(x='Mes', y='Total casos', data=casos, palette='muted')
    plt.title('Casos por mes')
    plt.xlabel('Mes')
    plt.ylabel('Total de casos')
    plt.show()

# Ejemplo de uso
if __name__ == "__main__":
    from src.data.cleaners import preparar_datos

    # Cargar y limpiar los datos
    ruta_archivo = "D:\\DATA_ANALIZAR.csv"
    datos_limpios = preparar_datos(ruta_archivo)

    # Llamar a las funciones para graficar
    graficar_producto_mas_ingresos(datos_limpios)
    graficar_ranking_problemas(datos_limpios)
    graficar_top_10_ejecutivos(datos_limpios)
    graficar_porcentaje_estados(datos_limpios)
    graficar_promedio_vida_util(datos_limpios)
    graficar_producto_menor_vida_util(datos_limpios)
    graficar_casos_por_mes(datos_limpios)
