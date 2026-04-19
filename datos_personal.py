# datos de los trabajadores del laboratorio 
#usar findall
#mdoficar contraseña con ultimas funciones r"^\d{}

import re
from modulo1 import pedir_opcion

texto1 = "Carlos Perez, telefono 1234-5678, direccion calle libertad 123, correo carlos.perez@email.com"
texto2 = "Javier Gomez, telefono 9876-5432, direccion calle libertad 456, correo javier.gomez@email.com"

def consultar_dato():
    
    """ Esta función sirve para consultar los datos de los trabajadores del laboratorio, permitiendo al usuario seleccionar el trabajador y el dato que desea conocer"""
    
    while True:
        print("\nSeleccione personal de laboratorio:")
        print("1. Carlos")
        print("2. Javier")
        print("3. Salir")
        opcion_persona = pedir_opcion("Seleccione numero: ", 1, 3)

        if opcion_persona == 3:
            print("Saliendo del programa...")
            return

        print("\nSeleccione el dato que desea conocer:")
        print("1. Telefono")
        print("2. Direccion")
        print("3. Correo")
        opcion_dato = pedir_opcion("Seleccione numero: ", 1, 3)

        if opcion_persona == 1:
            persona = "Carlos"
            texto = texto1
        else:
            persona = "Javier"
            texto = texto2

        if opcion_dato == 1:
            dato = "telefono"
            resultado = re.findall(r"\d{4}-\d{4}", texto)
        elif opcion_dato == 2:
            dato = "direccion"
            resultado = re.findall(r"direccion (.*?), correo", texto)
        else:
            dato = "correo"
            resultado = re.findall(r"[\w\.-]+@[\w\.-]+", texto)

        if resultado:
            print(f"El {dato} de {persona} es: {resultado[0]}")
        else:
            print(f"No se encontro el {dato} de {persona}")
