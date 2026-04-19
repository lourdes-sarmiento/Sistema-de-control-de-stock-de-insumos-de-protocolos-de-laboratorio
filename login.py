#Aquí se maneja la logica del login, verificación del usuario y contraseña, y el acceso al menu principal del sistema.
import datos
from modulo1 import menu
import re

def menu_entrada():
    
    """ Esta función sirve para mostrar el menú de entrada para iniciar sesión o crear una cuenta"""
    
    while True:
        print("BIENVENIDO AL MENU PRINCIPAL: ")
        print("1. Iniciar sesión")
        print("2. Crear cuenta")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            ingresar()

        elif opcion == "2":
            crear_cuenta()

        elif opcion == "3":
            print("Saliendo del sistema...")
            return

        else:
            print("Opción inválida")

def crear_cuenta():
    
    """ Esta función sirve para crear una nueva cuenta de usuario"""
    
    usuario = input("Ingrese un usuario: ")

    while True:
        contraseña = input("Ingrese una contraseña (debe terminar con al menos 2 números): ")

        if re.match(r".*\d{2,}$", contraseña):
            datos.lista_usuarios.append(usuario)
            datos.lista_contraseñas.append(contraseña)
            print("Cuenta creada con éxito")
            return
        else:
            print("Error: la contraseña debe terminar con al menos 2 números")


def login(usuario_ingresado, contraseña_ingresada, lista_usuarios, lista_contraseñas) :
    
    """ Esta función sirve para verificar si el usuario y la contraseña ingresados son correctos"""
    
    indice = 0
    while indice <len(lista_usuarios):
        if re.search(f"^{usuario_ingresado}$", lista_usuarios[indice], re.IGNORECASE) and lista_contraseñas[indice] == contraseña_ingresada:
            return True
        indice = indice + 1
    return False

def ingresar():
    
    """ Esta función sirve para manejar el proceso de inicio de sesión, verificando el usuario y la contraseña, y limitando los intentos de acceso"""
    
    conteo_errores = 0
    acceso = False
    while acceso == False:
        usuario_ingresado = input ("Ingrese su nombre de usuario: ")
        contraseña_ingresada = input ("Ingrese su contraseña: ")
        if login (usuario_ingresado, contraseña_ingresada, datos.lista_usuarios, datos.lista_contraseñas):
            acceso = True
            menu()

        else:
            conteo_errores +=1
            print ("usuario o contraseña incorrectos, intente nuevamente")
            
            if conteo_errores >= 3:
                print("ha intentado entrar demasiadas veces")
                print("SALIENDO DEL SISTEMA...")
                return

def main():
    menu_entrada()
