import json

#carga y guardado de datos de insumos en archivos JSON
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

#carga y guardado de estadisticas de uso de insumos en archivos JSON
def cargar_estadisticas_insumos():
    "Carga las estadísticas de uso de los insumos desde un archivo JSON. Si el archivo no existe, devuelve un diccionario vacío."
    
    try:
        archivo = open("estadisticas.json", "r", encoding="utf-8")
        estadisticas = json.load(archivo)
        archivo.close()
        return estadisticas

    except FileNotFoundError:
        print("El archivo estadisticas.json no existe")
        return {}

def guardar_estadisticas_insumos(estadisticas):
    "Guarda las estadísticas de uso de los insumos en un archivo JSON. Si el archivo no existe, lo crea."
    try:
        archivo = open("estadisticas.json", "w", encoding="utf-8")
        json.dump(estadisticas, archivo, indent=4, ensure_ascii=False)
        archivo.close()

    except FileNotFoundError:
        print("El archivo estadisticas.json no existe")

# Carga, guardado, agregado, modificacion y eliminacion de datos del personal en archivos JSON
def cargar_datos_personal():
    "Carga los datos del personal desde un archivo JSON. Si el archivo no existe, devuelve un diccionario vacío."
    try:
        archivo = open("datos_personal.json", "r", encoding="utf-8")
        datos_personal = json.load(archivo)
        archivo.close()
        return datos_personal
    except FileNotFoundError:
        print("El archivo datos_personal.json no existe")
        return {}

def guardar_datos_personal(datos_personal):
    "Guarda los datos del personal en un archivo JSON. Si el archivo no existe, lo crea."
    try:
        archivo = open("datos_personal.json", "w", encoding="utf-8")
        json.dump(datos_personal, archivo, indent=4, ensure_ascii=False)
        archivo.close()

    except FileNotFoundError:
        print("El archivo datos_personal.json no existe")

def agregar_personal(datos_nuevo):
    datos_personal = cargar_datos_personal()

    if not isinstance(datos_nuevo, dict):
        print("Los datos del personal deben ser un diccionario.")
        return False

    if "Nombre" not in datos_nuevo or "Telefono" not in datos_nuevo or "Direccion" not in datos_nuevo or "Correo" not in datos_nuevo or "Obra Social" not in datos_nuevo or "Estado Civil" not in datos_nuevo or "Edad" not in datos_nuevo:
        print("Faltan campos obligatorios.")
        return False

    nombre_nuevo = datos_nuevo["Nombre"].strip().lower()
    for persona in datos_personal.values():
        if persona.get("Nombre", "").strip().lower() == nombre_nuevo:
            print("Ya existe una persona con ese nombre.")
            return False

    numero_maximo = 0
    for clave in datos_personal:
        if clave.startswith("datos"):
            sufijo = clave[5:]
            if sufijo.isdigit():
                numero_maximo = max(numero_maximo, int(sufijo))

    clave_nueva = f"datos{numero_maximo + 1}"
    datos_personal[clave_nueva] = {
        "Nombre": datos_nuevo["Nombre"],
        "Telefono": datos_nuevo["Telefono"],
        "Direccion": datos_nuevo["Direccion"],
        "Correo": datos_nuevo["Correo"],
        "Obra Social": datos_nuevo["Obra Social"],
        "Estado Civil": datos_nuevo["Estado Civil"],
        "Edad": datos_nuevo["Edad"],
    }
    guardar_datos_personal(datos_personal)
    return True


def modificar_personal(nombre_persona, nuevos_datos):
    datos_personal = cargar_datos_personal()
    nombre_buscado = nombre_persona.strip().lower()
    clave_persona = None

    for clave, persona in datos_personal.items():
        if persona.get("Nombre", "").strip().lower() == nombre_buscado:
            clave_persona = clave
            break

    if clave_persona is None:
        print("No se encontro una persona con ese nombre.")
        return False

    if not isinstance(nuevos_datos, dict):
        print("Los nuevos datos deben ser un diccionario.")
        return False

    persona_actualizada = datos_personal[clave_persona]

    if "Nombre" in nuevos_datos and nuevos_datos["Nombre"] != "":
        persona_actualizada["Nombre"] = nuevos_datos["Nombre"]
    if "Telefono" in nuevos_datos and nuevos_datos["Telefono"] != "":
        persona_actualizada["Telefono"] = nuevos_datos["Telefono"]
    if "Direccion" in nuevos_datos and nuevos_datos["Direccion"] != "":
        persona_actualizada["Direccion"] = nuevos_datos["Direccion"]
    if "Correo" in nuevos_datos and nuevos_datos["Correo"] != "":
        persona_actualizada["Correo"] = nuevos_datos["Correo"]
    if "Obra Social" in nuevos_datos and nuevos_datos["Obra Social"] != "":
        persona_actualizada["Obra Social"] = nuevos_datos["Obra Social"]
    if "Estado Civil" in nuevos_datos and nuevos_datos["Estado Civil"] != "":
        persona_actualizada["Estado Civil"] = nuevos_datos["Estado Civil"]
    if "Edad" in nuevos_datos and nuevos_datos["Edad"] != "":
        persona_actualizada["Edad"] = nuevos_datos["Edad"]

    datos_personal[clave_persona] = persona_actualizada
    guardar_datos_personal(datos_personal)
    return True


def eliminar_personal(nombre_persona):
    datos_personal = cargar_datos_personal()
    nombre_buscado = nombre_persona.strip().lower()
    clave_persona = None

    for clave, persona in datos_personal.items():
        if persona.get("Nombre", "").strip().lower() == nombre_buscado:
            clave_persona = clave
            break

    if clave_persona is None:
        print("No se encontro una persona con ese nombre.")
        return False

    del datos_personal[clave_persona]
    guardar_datos_personal(datos_personal)
    return True
