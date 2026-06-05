import json

def cargar_datos_insumos():
    "Carga los datos de los insumos desde un archivo JSON. Si el archivo no existe, devuelve un diccionario vacío."
    
    try:
        archivo = open("datos_insumos.json", "r", encoding="utf-8")
        datos_insumos = json.load(archivo)
        archivo.close()
        return datos_insumos

    except FileNotFoundError:
        print("El archivo datos_insumos.json no existe")
        return {}

def guardar_datos_insumos(datos_insumos):
    "Guarda los datos de los insumos en un archivo JSON. Si el archivo no existe, lo crea."
    try:
        archivo = open("datos_insumos.json", "w", encoding="utf-8")
        json.dump(datos_insumos, archivo, indent=4, ensure_ascii=False)
        archivo.close()

    except FileNotFoundError:
        print("El archivo datos_insumos.json no existe")