# datos de los trabajadores del laboratorio
 
import re
from modulo1 import pedir_opcion
 
import re

from funciones_cargapermanente import cargar_datos_personal
from modulo1 import pedir_opcion


def mostrar_valores_en_comun():
    """Muestra los valores en comun entre todas las parejas de registros cargados."""
    datos_personal = cargar_datos_personal()
    personas = list(datos_personal.values())

    if len(personas) < 2:
        print("Se necesitan al menos dos personas cargadas para comparar datos en comun.")
        return

    print("\nDatos en común entre los trabajadores:")
    for indice1 in range(len(personas)):
        for indice2 in range(indice1 + 1, len(personas)):
            persona1 = personas[indice1]
            persona2 = personas[indice2]
            valores_en_comun = set(persona1.values()).intersection(set(persona2.values()))

            if valores_en_comun:
                print(f"{persona1['Nombre']} y {persona2['Nombre']} tienen estos datos en comun:")
                for valor in valores_en_comun:
                    print(valor)
            else:
                print(f"{persona1['Nombre']} y {persona2['Nombre']} no tienen datos en comun.")


def consultar_dato():
    """Consulta los datos del personal cargados en el JSON."""
    datos_personal = cargar_datos_personal()
    personas = list(datos_personal.values())

    if not personas:
        print("No hay personal cargado.")
        return

    while True:
        print("\nSeleccione personal de laboratorio:")
        for indice, persona in enumerate(personas, start=1):
            print(f"{indice}. {persona.get('Nombre', 'Sin nombre')}")
        print(f"{len(personas) + 1}. Mostrar datos en común entre todos los trabajadores")
        print(f"{len(personas) + 2}. Salir")

        opcion_persona = pedir_opcion("Seleccione numero: ", 1, len(personas) + 2)

        if opcion_persona == len(personas) + 1:
            mostrar_valores_en_comun()
            continue
        if opcion_persona == len(personas) + 2:
            print("Saliendo del programa...")
            return

        persona = personas[opcion_persona - 1]

        print("\nSeleccione el dato que desea conocer:")
        opciones = {}
        numero = 1

        for clave, valor in persona.items():
            if clave != "Nombre":
                print(f"{numero}. {clave}")
                opciones[numero] = clave
                numero += 1

        print(f"{numero}. Todos los datos del empleado de laboratorio")
        opciones[numero] = "Todos"

        opcion_dato = pedir_opcion("Seleccione numero: ", 1, len(opciones))
        dato_elegido = opciones[opcion_dato]

        if dato_elegido == "Todos":
            print(f"\nDatos de {persona['Nombre']}:")
            for clave, valor in persona.items():
                print(f"{clave}: {valor}")
        else:
            texto = f"{dato_elegido}: {persona[dato_elegido]}"

            if dato_elegido == "Telefono":
                resultado = re.findall(r"\d{4}-\d{4}", texto)
            elif dato_elegido == "Direccion":
                resultado = [persona[dato_elegido]] if persona[dato_elegido] else []
            elif dato_elegido == "Correo":
                resultado = re.findall(r"[\w\.-]+@[\w\.-]+", texto)
            elif dato_elegido == "Obra Social":
                resultado = [persona[dato_elegido]] if persona[dato_elegido] else []
            elif dato_elegido == "Estado Civil":
                resultado = [persona[dato_elegido]] if persona[dato_elegido] else []
            elif dato_elegido == "Edad":
                resultado = [persona[dato_elegido]] if persona[dato_elegido] else []
            else:
                resultado = []

            if resultado:
                print(f"El {dato_elegido} de {persona['Nombre']} es: {resultado[0]}")
            else:
                print(f"No se encontro el {dato_elegido} de {persona['Nombre']}")
