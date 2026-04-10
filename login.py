#Aquí se maneja la logica del login, verificación del usuario y contraseña, y el acceso al menu principal del sistema.
import datos
from modulo1 import menu

def login(usuario_ingresado, contraseña_ingresada, lista_usuarios, lista_contraseñas) :
    indice = 0
    while indice <len(lista_usuarios):
        if lista_usuarios[indice] == usuario_ingresado and lista_contraseñas [indice] == contraseña_ingresada :
            return True
        indice = indice + 1
    return False

def ingresar():
    acceso = False
    while acceso == False:
        usuario_ingresado = input ("Ingrese su nombre de usuario: ")
        contraseña_ingresada = input ("Ingrese su contraseña: ")
        if login (usuario_ingresado, contraseña_ingresada, datos.lista_usuarios, datos.lista_contraseñas):
            acceso = True
            menu()
        else:
            print ("usuario o contraseña incorrectos, intente nuevamente")