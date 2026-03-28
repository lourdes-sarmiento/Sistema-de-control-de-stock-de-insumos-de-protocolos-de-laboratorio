#listas de usuarios y contraseñas para el login
lista_usuarios = ["carlos" , "javier"]
lista_contraseñas = ["1" , "2"]


def login(usuario_ingresado, contraseña_ingresada, lista_usuarios, lista_contraseñas) :
    indice = 0
    while indice <len(lista_usuarios):
        if lista_usuarios[indice] == usuario_ingresado and lista_contraseñas [indice] == contraseña_ingresada :
            return True
        indice = indice + 1
    return False


#programa principal
usuario_ingresado = input ("ingrese su nombre de usuario: ")
contraseña_ingresada = input ("ingrese su contraseña: ")
if login (usuario_ingresado, contraseña_ingresada, lista_usuarios, lista_contraseñas):
    login_exitoso = True
    print("bienvenido")
else:
    print ("usuario o contraseña incorrectos, intente nuevamente")
