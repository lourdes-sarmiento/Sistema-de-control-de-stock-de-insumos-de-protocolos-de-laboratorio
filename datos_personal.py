# datos de los trabajadores del laboratorio
 
import re
from modulo1 import pedir_opcion
 
datos1={"Nombre":"Carlos Perez",
       "Telefono":"1234-5678",
       "Direccion":"calle libertad 123",
       "Correo":"carlos.perez@email.com",
       "Obra Social":"OSDE",
       "Estado Civil":"Casado",
       "Edad":"30 años"
   
       }
 
datos2={"Nombre":"Javier Gomez",
       "Telefono":"9876-5432",
       "Direccion":"calle libertad 456",
       "Correo":"javier.gomez@email.com",
       "Obra Social":"Swiss Medical",
       "Estado Civil":"Casado",
       "Edad":"30 años"
       }
 
 
def mostrar_valores_en_comun():
    """ Esta función muestra los datos que ambos trabajadores del laboratorio tienen en común,
    como su edad y estado civil, se utiliza sets para encontrar 
    los valores en común entre ambos diccionarios de datos"""
    valores_datos1 = set(datos1.values())
    valores_datos2 = set(datos2.values())
 
    valores_en_comun = valores_datos1.intersection(valores_datos2)
 
    print("\nDatos en común entre ambos trabajadores:")
    for valor in valores_en_comun:
        print(valor)
 
 
def consultar_dato():
   
    """ Esta función sirve para consultar los datos de los trabajadores del laboratorio, permitiendo al usuario seleccionar el trabajador y el dato que desea conocer o todos sus datos"""
   
    while True:
        print("\nSeleccione personal de laboratorio:")
        print("1. Carlos")
        print("2. Javier")
        print("3. Mostrar datos en común entre ambos trabajadores")
        print("4. Salir")
        opcion_persona = pedir_opcion("Seleccione numero: ", 1, 4)
 
        if opcion_persona == 3:
            mostrar_valores_en_comun()
        elif opcion_persona == 4:
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
            elif dato_elegido == "Obra Social":
                resultado = re.findall(r"Obra Social: (.*?)$", texto)
            elif dato_elegido == "Estado Civil":
                resultado = re.findall(r"Estado Civil: (.*?)$", texto)
            elif dato_elegido == "Edad":
                resultado = re.findall(r"Edad: (\d+ años)", texto)
 
            if resultado:
                print(f"El {dato_elegido} de {persona['Nombre']} es: {resultado[0]}")
            else:
                print(f"No se encontro el {dato_elegido} de {persona['Nombre']}")
 

