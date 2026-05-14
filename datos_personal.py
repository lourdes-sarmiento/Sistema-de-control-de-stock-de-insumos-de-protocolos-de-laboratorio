# datos de los trabajadores del laboratorio 

import re
from modulo1 import pedir_opcion

datos1={"Nombre":"Carlos Perez",
       "Telefono":"1234-5678",
       "Direccion":"calle libertad 123",
       "Correo":"carlos.perez@email.com",
       "Obra Social":"OSDE"
       }

datos2={"Nombre":"Javier Gomez",
       "Telefono":"9876-5432",
       "Direccion":"calle libertad 456",
       "Correo":"javier.gomez@email.com",
       "Obra Social":"Swiss Medical"
       }

def consultar_dato():
    
    """ Esta función sirve para consultar los datos de los trabajadores del laboratorio, permitiendo al usuario seleccionar el trabajador y el dato que desea conocer o todos sus datos"""
    
    while True:
        print("\nSeleccione personal de laboratorio:")
        print("1. Carlos")
        print("2. Javier")
        print("3. Salir")
        opcion_persona = pedir_opcion("Seleccione numero: ", 1, 3)

        if opcion_persona == 3:
            print("Saliendo del programa...")
            return
        
        if opcion_persona == 1:
            persona = datos1
            
        else:
            persona = datos2

        print("\nSeleccione el dato que desea conocer:")
        
        opciones={}
        
        numero=1
        for clave,valor in persona.items():
            if clave!="Nombre":
                print(f"{numero}. {clave}")
                opciones[numero]=clave
                numero+=1
                
        print(f"{numero}. Todos los datos del empleado de laboratorio")
        opciones[numero]="Todos"
        
        opcion_dato = pedir_opcion("Seleccione numero: ", 1, len(opciones))
        dato_elegido=opciones[opcion_dato]
        
        if dato_elegido == "Todos":
            print(f"\nDatos de {persona['Nombre']}:")
            for clave, valor in persona.items():
                print(f"{clave}: {valor}")
        
        else:
            texto=f"{dato_elegido}: {persona[dato_elegido]}"
            
            if dato_elegido == "Telefono":
                resultado = re.findall(r"\d{4}-\d{4}", texto)
            elif dato_elegido == "Direccion":
                resultado = re.findall(r"Direccion: (.*?), correo", texto)
            elif dato_elegido == "Correo":
                resultado = re.findall(r"[\w\.-]+@[\w\.-]+", texto)
            else:
                resultado = re.findall(r"Obra Social: (.*?)$", texto)

            if resultado:
                print(f"El {dato_elegido} de {persona['Nombre']} es: {resultado[0]}")
            else:
                print(f"No se encontro el {dato_elegido} de {persona['Nombre']}")

