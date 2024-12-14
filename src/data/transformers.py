import pandas as pd
from src.data.cleaners import preparar_datos

# Cargar y limpiar los datos
data_limpia = preparar_datos("D:\\DATA_ANALIZAR.csv")


# Función para obtener el mes con mayor ingreso a técnico
def mes_mayor_ingreso(data_limpia: pd.DataFrame) -> str:
    data_limpia['FECHA INGRESO'] = pd.to_datetime(data_limpia['FECHA INGRESO'], errors='coerce')
    incidencias_mes = data_limpia['FECHA INGRESO'].dt.month.value_counts()
    mes_con_mayor_ingreso = incidencias_mes.idxmax()
    meses_nombres = {
        1: "Enero", 2: "Febrero", 3: "Marzo", 4: "Abril", 5: "Mayo",
        6: "Junio", 7: "Julio", 8: "Agosto", 9: "Septiembre",
        10: "Octubre", 11: "Noviembre", 12: "Diciembre"
    }
    return meses_nombres.get(mes_con_mayor_ingreso, "Mes desconocido")

# Función para obtener el SKU y producto con más ingresos registrados
def producto_mas_ingresos(data_limpia: pd.DataFrame) -> pd.DataFrame:
    producto_ingresos = data_limpia.groupby(['CODIGO PRODUCTO', 'PRODUCTO']).size().reset_index(name='Total ingresos')
    producto_top = producto_ingresos.sort_values(by='Total ingresos', ascending=False).head(1)
    return producto_top

# Función para generar el ranking de los principales problemas registrados
def ranking_problemas(data_limpia: pd.DataFrame) -> pd.DataFrame:
    ranking = data_limpia['PROBLEMA'].value_counts().reset_index()
    ranking.columns = ['Problema', 'Total casos']
    return ranking

# Función para obtener el ejecutivo con más casos atendidos
def ejecutivo_mas_casos(data_limpia: pd.DataFrame) -> pd.DataFrame:
    ejecutivo_casos = data_limpia['EJECUTIVO'].value_counts().reset_index()
    ejecutivo_casos.columns = ['Ejecutivo', 'Total casos']
    return ejecutivo_casos.head(1)

def porcentaje_estados(data_limpia: pd.DataFrame) -> pd.DataFrame:
    # Obtener el conteo de cada estado con su proporción (porcentaje)
    estado_casos = data_limpia['ESTADO CASO'].value_counts(normalize=True) * 100
    # Resetear el índice y cambiar los nombres de las columnas manualmente
    resultado = estado_casos.reset_index()
    resultado.columns = ['Estado', 'Porcentaje']  # Renombrar las columnas
    return resultado



    # Función para calcular el promedio de vida útil del producto (días, extraído de TIEMPO DE USO)
def promedio_vida_util(data_limpia: pd.DataFrame) -> float:
    data_limpia['TIEMPO DE USO'] = pd.to_numeric(data_limpia['TIEMPO DE USO'], errors='coerce')
    promedio_vida = data_limpia['TIEMPO DE USO'].mean()
    return promedio_vida

def producto_menor_vida_util(data_limpia: pd.DataFrame) -> pd.DataFrame:
    # Asegurarse de que 'TIEMPO DE USO' esté en formato numérico
    data_limpia['TIEMPO DE USO'] = pd.to_numeric(data_limpia['TIEMPO DE USO'], errors='coerce')
    
    # Agrupar por producto y calcular el promedio de 'TIEMPO DE USO'
    producto_menor_vida = data_limpia.groupby(['CODIGO PRODUCTO', 'PRODUCTO'])['TIEMPO DE USO'].mean().reset_index()
    
    # Ordenar por el 'TIEMPO DE USO' de menor a mayor y seleccionar el primer producto
    producto_menor_vida = producto_menor_vida.sort_values(by='TIEMPO DE USO').head(1)
    
    # Convertir el tiempo de uso a valor absoluto (en caso de que haya valores negativos)
    producto_menor_vida['TIEMPO DE USO ABSOLUTO'] = producto_menor_vida['TIEMPO DE USO'].abs()
    
    return producto_menor_vida[['CODIGO PRODUCTO', 'PRODUCTO', 'TIEMPO DE USO', 'TIEMPO DE USO ABSOLUTO']]


# Función para obtener el Top 10 de ejecutivos con más casos atendidos, ordenado de mayor a menor
def top_10_ejecutivos(data_limpia: pd.DataFrame) -> pd.DataFrame:
    # Contar la cantidad de casos atendidos por cada ejecutivo
    ejecutivo_casos = data_limpia['EJECUTIVO'].value_counts().reset_index()
    ejecutivo_casos.columns = ['Ejecutivo', 'Total casos']
    
    # Ordenar de mayor a menor y seleccionar los primeros 10
    top_10 = ejecutivo_casos.sort_values(by='Total casos', ascending=False).head(10)
    
    return top_10


# Función para calcular el total de casos por mes, ordenado de mayor a menor
def casos_por_mes(data_limpia: pd.DataFrame) -> pd.DataFrame:
    # Convertir la columna FECHA INGRESO a formato datetime
    data_limpia['FECHA INGRESO'] = pd.to_datetime(data_limpia['FECHA INGRESO'], errors='coerce')
    
    # Extraer el mes de la columna FECHA INGRESO
    data_limpia['Mes'] = data_limpia['FECHA INGRESO'].dt.month
    
    # Contar el total de casos por mes
    casos_mes = data_limpia.groupby('Mes').size().reset_index(name='Total casos')
    
    # Diccionario de nombres de meses
    meses_nombres = {
        1: "Enero", 2: "Febrero", 3: "Marzo", 4: "Abril", 5: "Mayo",
        6: "Junio", 7: "Julio", 8: "Agosto", 9: "Septiembre",
        10: "Octubre", 11: "Noviembre", 12: "Diciembre"
    }
    
    # Mapear los números de mes a nombres
    casos_mes['Mes'] = casos_mes['Mes'].map(meses_nombres)
    
    # Ordenar los casos de mayor a menor
    casos_mes = casos_mes.sort_values(by='Total casos', ascending=False)
    
    return casos_mes



# Generar resultados
print("Mes con mayor ingreso:", mes_mayor_ingreso(data_limpia))
print("Producto con más ingresos registrados:")
print(producto_mas_ingresos(data_limpia))
print("Ranking de principales problemas:")
print(ranking_problemas(data_limpia))
print("Ejecutivo con más casos atendidos:")
print(ejecutivo_mas_casos(data_limpia))
print("Total de casos atendidos por ejecutivo:")
print(top_10_ejecutivos(data_limpia))
print("Porcentaje de estados abiertos/cerrados:")
print(porcentaje_estados(data_limpia))
print("Promedio de vida útil del producto:", promedio_vida_util(data_limpia), "días")
print("Producto con menor vida útil:")
print(producto_menor_vida_util(data_limpia))
print("Ingresos por mes a incidencias:")
print(casos_por_mes(data_limpia))
