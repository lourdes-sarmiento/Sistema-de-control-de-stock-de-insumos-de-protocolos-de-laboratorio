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
        try:
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
        except ValueError:
            print("Error: Entrada no válida. Por favor, ingrese un número correspondiente a las opciones del menú.")
            
def crear_cuenta():

    
    """ Esta función sirve para crear una nueva cuenta de usuario"""
    
    usuario = input("Ingrese un usuario: ")

    while True:
        contraseña = input("Ingrese una contraseña (debe terminar con al menos 2 números): ")

        if usuario in datos.usuarios:
            print(f"Error: El usuario '{usuario}' ya está registrado. Intente con otro.")
            return

        if re.match(r".*\d{2,}$", contraseña) and len(usuario) > 0:
            datos.usuarios[usuario] = contraseña
            datos.lista_usuarios.append(usuario)
            datos.lista_contraseñas.append(contraseña)
            print("Cuenta creada con éxito")
            return
        else:
            print("Error: la contraseña debe terminar con al menos 2 números o el campo usuario no fue llenado.")
            return


def login(usuario_ingresado, contraseña_ingresada, lista_usuarios, lista_contraseñas) :
    
    """ Esta función sirve para verificar si el usuario y la contraseña ingresados son correctos se utliza"""
    """ Se utliza una búsqueda con expresiones regulares para comparar el usuario ingresado con la lista de usuarios, y se verifica que la contraseña coincida con la contraseña correspondiente al usuario encontrado"""
    """ Se utiliza tercer parametro re.IGNORECASE para hacer la búsqueda de usuarios sin importar mayúsculas o minúsculas"""
    indice = 0
    while indice <len(lista_usuarios):
        if re.search(f"^{usuario_ingresado}$", lista_usuarios[indice], re.IGNORECASE) and lista_contraseñas[indice] == contraseña_ingresada:
            return True
        indice = indice + 1
    return False

def ingresar(conteo_errores=0):
    """ Esta función sirve para manejar el proceso de inicio de sesión, verificando el usuario y la contraseña, y limitando los intentos de acceso"""
    
    if conteo_errores >= 3:
        print("Ha intentado entrar demasiadas veces.")
        print("SALIENDO DEL SISTEMA...")
        exit()

    usuario_ingresado = input("Ingrese su nombre de usuario: ")
    contraseña_ingresada = input("Ingrese su contraseña: ")
    
    if login(usuario_ingresado, contraseña_ingresada, datos.lista_usuarios, datos.lista_contraseñas):
        menu()
    else:
        print("Usuario o contraseña incorrectos, intente nuevamente.")
        ingresar(conteo_errores + 1)

def main():
    menu_entrada()

