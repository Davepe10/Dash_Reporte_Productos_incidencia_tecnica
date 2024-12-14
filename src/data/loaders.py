import pandas as pd
import warnings
def cargar_datos_csv(ruta_csv: str):
  ruta_csv = r"D:\DATA_ANALIZAR.csv"
  try:
   with warnings.catch_warnings():
     warnings.simplefilter("ignore")
     data_csv = pd.read_csv(ruta_csv)
     data = data_csv.copy()
     return data

  except FileNotFoundError as e:
    print(f"Error: No se encontró el archivo. Verifica la ruta: {e}")
  except Exception as e:
    print(f"Ha ocurrido un error: {e}")
 


data = cargar_datos_csv("D:\\DATA_ANALIZAR.csv")
print(data.head(10))

