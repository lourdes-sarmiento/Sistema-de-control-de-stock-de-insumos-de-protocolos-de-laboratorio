
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

#funciones para mostrar los insumos y procesos basicos de cada protocolo, y para pedir opciones al usuario en los menus

def pedir_opcion(mensaje, minimo, maximo):
    '''Pide al usuario que ingrese una opcion entre minimo y maximo.'''
    opcion = int(input(mensaje))
    while opcion < minimo or opcion > maximo:
        print(f"Ingrese una opcion entre {minimo} y {maximo}.")
        opcion = int(input(mensaje))
    return opcion


def mostrar_insumos_pcr():
    '''Muestra los insumos necesarios para el protocolo PCR.'''
    insumos = [
        ["PCR", "Primers", 6, "unidades", "<= 2"],
        ["", "dNTPs", 5, "unidades", "<= 2"],
        ["", "ADN Polimerasa", 4, "frascos", "<= 2"],
        ["", "Cofactor", 5, "unidades", "<= 2"],
        ["", "Buffer de PCR", 6, "frascos", "<= 2"],
        ["", "Tubos de PCR", 10, "unidades", "<= 2"]
    ]

    print()
    print("Insumos del protocolo PCR:")
    print("Protocolo |  Insumo     |     Stock |  Unidad  |   Alerta en")
    print("--------------------------------------------------------------")

    for i in range(len(insumos)):
        print(f"{insumos[i][0]:<11} {insumos[i][1]:<18} {insumos[i][2]:<7} {insumos[i][3]:<11} {insumos[i][4]}")



def mostrar_proceso_basico_pcr():
    '''Muestra el proceso basico del protocolo PCR.'''
    print()
    print("Proceso basico del protocolo PCR:")
    print("1. Preparar la mezcla de reaccion.")
    print("2. Colocar los tubos en el termociclador.")
    print("3. Configurar los ciclos de desnaturalizacion, alineamiento y extension.")
    print("4. Esperar la finalizacion del proceso.")
    print("5. Conservar el producto para su analisis.")


def mostrar_insumos_electroforesis():
    '''Muestra los insumos necesarios para el protocolo Electroforesis.'''
    insumos = [
        ["Electroforesis", "Gel de agarosa", 6, "frascos", "<= 2"],
        ["", "Buffer de corrida", 8, "frascos", "<= 2"],
        ["", "Agente intercalante", 5, "frascos", "<= 2"],
        ["", "Marcador peso mol.", 5, "unidades", "<= 2"]
    ]

    print()
    print("Insumos del protocolo Electroforesis:")
    print("Protocolo   |   Insumo      |      Stock  | Unidad      |   Alerta en")
    print("----------------------------------------------------------------")

    for i in range(len(insumos)):
        print(f"{insumos[i][0]:<15} {insumos[i][1]:<18} {insumos[i][2]:<7} {insumos[i][3]:<11} {insumos[i][4]}")


def mostrar_insumos_extraccion_adn():
    '''Muestra los insumos necesarios para el protocolo Extraccion de ADN.'''
    insumos = [
        ["Extraccion de ADN", "Buffer de lisis", 7, "frascos", "<= 2"],
        ["", "Enzimas", 6, "frascos", "<= 2"],
        ["", "Agentes de separacion", 4, "frascos", "<= 2"],
        ["", "Alcoholes", 5, "frascos", "<= 2"],
        ["", "Buffer de elucion", 6, "frascos", "<= 2"]
    ]

    print()
    print("Insumos del protocolo Extraccion de ADN:")
    print("Protocolo      |    Insumo         |       Stock  | Unidad      |   Alerta en")
    print("-------------------------------------------------------------------------")

    for i in range(len(insumos)):
        print(f"{insumos[i][0]:<20} {insumos[i][1]:<23} {insumos[i][2]:<7} {insumos[i][3]:<11} {insumos[i][4]}")


def mostrar_proceso_basico_electroforesis():
    '''Muestra el proceso basico del protocolo Electroforesis.'''
    print()
    print("Proceso basico del protocolo Electroforesis:")
    print("1. Preparar el gel de agarosa.")
    print("2. Colocar el gel en la camara de corrida.")
    print("3. Agregar buffer de corrida.")
    print("4. Cargar las muestras y el marcador.")
    print("5. Conectar la fuente y realizar la corrida.")


def mostrar_proceso_basico_extraccion_adn():
    '''Muestra el proceso basico del protocolo Extraccion de ADN.'''
    print()
    print("Proceso basico del protocolo Extraccion de ADN:")
    print("1. Colocar la muestra en un tubo.")
    print("2. Agregar buffer de lisis.")
    print("3. Incorporar enzimas y agentes de separacion.")
    print("4. Realizar los lavados con alcohol.")
    print("5. Recuperar el ADN con buffer de elucion.")


def menu_pcr():
    '''Muestra el menu del protocolo PCR.'''
    opcion = 0
    while opcion != 3:
        print()
        print("Menu del Protocolo PCR")
        print("------------------------")
        print("1. Ver insumos y cantidades")
        print("2. Ver proceso basico")
        print("3. Volver al menu principal")

        opcion = pedir_opcion("Seleccione una opcion: ", 1, 3)

        if opcion == 1:
            mostrar_insumos_pcr()
        elif opcion == 2:
            mostrar_proceso_basico_pcr()
        elif opcion == 3:
            print("Volviendo al menu principal...")


def menu_electroforesis():
    '''Muestra el menu del protocolo Electroforesis.'''
    opcion = 0
    while opcion != 3:
        print()
        print("Menu del Protocolo Electroforesis")
        print("---------------------------------")
        print("1. Ver insumos y cantidades")
        print("2. Ver proceso basico")
        print("3. Volver al menu principal")

        opcion = pedir_opcion("Seleccione una opcion: ", 1, 3)

        if opcion == 1:
            mostrar_insumos_electroforesis()
        elif opcion == 2:
            mostrar_proceso_basico_electroforesis()
        elif opcion == 3:
            print("Volviendo al menu principal...")


def menu_extraccion_adn():
    '''Muestra el menu del protocolo Extraccion de ADN.'''
    opcion = 0
    while opcion != 3:
        print()
        print("Menu del Protocolo Extraccion de ADN")
        print("-------------------------------------")
        print("1. Ver insumos y cantidades")
        print("2. Ver proceso basico")
        print("3. Volver al menu principal")

        opcion = pedir_opcion("Seleccione una opcion: ", 1, 3)

        if opcion == 1:
            mostrar_insumos_extraccion_adn()
        elif opcion == 2:
            mostrar_proceso_basico_extraccion_adn()
        elif opcion == 3:
            print("Volviendo al menu principal...")


def menu():
    '''Muestra el menu principal del programa.'''
    dato=0
    while dato != 4:
        print("***********************************************************************************")
        print("Bienvenido al programa de control de insumos y protocolos de Laboratorios Umbrella")
        print("***********************************************************************************")
        print("1. Protocolo PCR")
        print("2. Protocolo Electroforesis")
        print("3. Protocolo Extraccion de ADN")
        print("4. Salir del programa")
        print()

        dato = pedir_opcion("Ingrese opcion de protocolo a realizar: ", 1, 4)

        if dato == 1:
            print("Has seleccionado el protocolo PCR")
            menu_pcr()
        elif dato == 2:
            print("Has seleccionado el protocolo Electroforesis")
            menu_electroforesis()
        elif dato == 3:
            print("Has seleccionado el protocolo Extraccion de ADN")
            menu_extraccion_adn()
        elif dato == 4:
            print("Has seleccionado salir del programa")


menu()
