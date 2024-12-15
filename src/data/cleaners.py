# src/data/cleaners.py
import pandas as pd
from src.data.loaders import cargar_datos_csv
from rapidfuzz import process, fuzz

def eliminar_columnas_irrelevantes(dataset: pd.DataFrame) -> pd.DataFrame:
    columnas_eliminar = ['FECHA DE ENTREGA', 'NOMBRE DEL PICKEADOR O CLIENTE', 'Repuesto Requerido','FECHA LISTO PARA RETIRO ','OBSERVACION',
                         'TECNICO','2) INFORME TECNICO	FECHA DE REPARACIÓN','2) TECNICO A CARGO','1) INFORME TECNICO',
                '1) TECNICO A CARGO','Fecha de revisión técnico','Número de telefono','NOMBRE CLIENTE','DETALLE PROBLEMA',
            ' FECHA DE COMPRA','Unnamed: 26', 'ESTADO']
    dataset = dataset.drop(columns=columnas_eliminar, axis=1, errors='ignore')
    return dataset

def crear_id(dataset: pd.DataFrame) -> pd.DataFrame:
    dataset['ID'] = [f'{i:03}' for i in range(1, len(dataset) + 1)]
    return dataset

def eliminar_filas_nulas(dataset: pd.DataFrame) -> pd.DataFrame:
    dataset = dataset.replace(r'^\s*$', pd.NA, regex=True)
    dataset = dataset.dropna(how='all')
    dataset = dataset[~dataset.iloc[:, :-1].isnull().all(axis=1)]
    return dataset

def cambiar_nombre_columna(dataset: pd.DataFrame) -> pd.DataFrame:
    dataset.rename(columns={ 'SKU': 'CODIGO PRODUCTO', 'TPO. USO':'TIEMPO DE USO', 'PROBLEMA  (SELECCIONAR DE LA LISTA DESPLEGABLE)': 'PROBLEMA'}, inplace=True, errors='ignore')
    return dataset

def limpiar_nombres(dataset: pd.DataFrame, columna: str) -> pd.DataFrame:
    dataset[columna] = dataset[columna].str.strip().str.lower().str.replace(r'\s+', ' ', regex=True)
    nombres_unicos = dataset[columna].unique()
    mapping = {}
    for nombre in nombres_unicos:
        mejor_match = process.extractOne(nombre, mapping.keys(), scorer=fuzz.ratio)
        if mejor_match and mejor_match[1] > 85:
            mapping[nombre] = mejor_match[0]
        else:
            mapping[nombre] = nombre
    dataset[columna] = dataset[columna].map(mapping)
    return dataset

def preparar_datos(dataset: str) -> pd.DataFrame:
    # Cargar los datos
    dataset = cargar_datos_csv("data_file/DATA_ANALIZAR.csv")
    # Limpiar los datos paso por paso
    dataset = eliminar_columnas_irrelevantes(dataset)
    dataset = crear_id(dataset)
    dataset = eliminar_filas_nulas(dataset)
    dataset = cambiar_nombre_columna(dataset)
    dataset = limpiar_nombres(dataset, 'PRODUCTO')
    
    return dataset


ruta_archivo = "data_file/DATA_ANALIZAR.csv"
dataset = preparar_datos(ruta_archivo)

# Verificar si el dataset fue procesado
if dataset is not None:
    print("Primeras 5 filas del dataset limpio:")
    print(dataset.head(5))
    # Guardar los datos limpios para corroborar
    dataset.to_csv("data_file/DATA_ANALIZAR.csv", index=False)
    print("Archivo limpio guardado como 'DATA_LIMPIO.csv'.")