import datos

def login(usuario_ingresado, contraseña_ingresada, lista_usuarios, lista_contraseñas) :
    indice = 0
    while indice <len(lista_usuarios):
        if lista_usuarios[indice] == usuario_ingresado and lista_contraseñas [indice] == contraseña_ingresada :
            return True
        indice = indice + 1
    return False

#funciones para mostrar los insumos y procesos basicos de cada protocolo, y para pedir opciones al usuario en los menus

def pedir_opcion(mensaje, minimo, maximo):
    '''Pide al usuario que ingrese una opcion entre minimo y maximo.'''
    opcion = int(input(mensaje))
    while opcion < minimo or opcion > maximo:
        print(f"Ingrese una opcion entre {minimo} y {maximo}.")
        opcion = int(input(mensaje))
    return opcion

def alertar_stock_bajo(insumos):
    '''Genera alertas para los insumos con stock menor o igual a 2 usando lista por comprension.'''
    return [
        f"Alerta: {insumo[1]} tiene {insumo[2]} {insumo[3]} disponible(s). Se debe reabastecer."
        for insumo in insumos if insumo[2] <= 2
    ]


def solicitar_uso_insumo(insumos):
    '''Solicita el insumo a utilizar y la cantidad de stock a descontar.'''
    print()
    print("Seleccione el insumo que va a utilizar:")
    print()

    for i in range(len(insumos)):
        print(f"{i + 1}. {insumos[i][1]} - Stock disponible: {insumos[i][2]} {insumos[i][3]}")
        print()
    opcion_insumo = pedir_opcion("Ingrese el numero del insumo: ", 1, len(insumos))
    insumo_seleccionado = insumos[opcion_insumo - 1]

    cantidad = int(input(f"Ingrese la cantidad de {insumo_seleccionado[1]} a utilizar: "))
    while cantidad < 1 or cantidad > insumo_seleccionado[2]:
        print("Cantidad invalida. Debe ser mayor a 0 y no superar el stock disponible.")
        cantidad = int(input(f"Ingrese la cantidad de {insumo_seleccionado[1]} a utilizar: "))

    stock_disponible = insumo_seleccionado[2]
    stock_restante = insumo_seleccionado[2] - cantidad
    insumo_seleccionado[2] = stock_restante

    print()
    print(f"Insumo seleccionado: {insumo_seleccionado[1]}")
    print(f"Stock disponible: {stock_disponible} {insumo_seleccionado[3]}")
    print(f"Cantidad a utilizar: {cantidad} {insumo_seleccionado[3]}")
    print(f"Stock restante: {stock_restante} {insumo_seleccionado[3]}")

    alertas = alertar_stock_bajo([insumo_seleccionado])
    if alertas:
        print()
        for alerta in alertas:
            print(alerta)

def menu_pcr():
    '''Muestra el menu del protocolo PCR.'''
    opcion = 0
    while opcion != 3:
        print()
        print("Menu del Protocolo PCR")
        print("------------------------")
        print("1. Ver insumos y cantidades")#seleccione el insumo luego seleccione la cantidad a utilizar.
        print("2. Ver proceso basico")
        print("3. Volver al menu principal")

        opcion = pedir_opcion("Seleccione una opcion: ", 1, 3)

        if opcion == 1:
            insumos = mostrar_insumos_pcr()
            solicitar_uso_insumo(insumos)
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
            insumos = mostrar_insumos_electroforesis()
            solicitar_uso_insumo(insumos)
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
            insumos = mostrar_insumos_extraccion_adn()
            solicitar_uso_insumo(insumos)
        elif opcion == 2:
            mostrar_proceso_basico_extraccion_adn()
        elif opcion == 3:
            print("Volviendo al menu principal...")


def menu():
    '''Muestra el menu principal del programa.'''
    dato=0
    while dato != 5:
        print("***********************************************************************************")
        print("Bienvenido al programa de control de insumos y protocolos de Laboratorios Umbrella")
        print("***********************************************************************************")
        print("1. Protocolo PCR")
        print("2. Protocolo Electroforesis")
        print("3. Protocolo Extraccion de ADN")
        print("4. Agregar stock")
        print("5. Salir del programa")
        print()

        dato = pedir_opcion("Ingrese opcion de protocolo a realizar: ", 1, 5)

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
            print("Has seleccionado agregar stock para un insumo")
            agregar_stock()
        elif dato == 5:
            print("Has seleccionado salir del programa")


def mostrar_insumos_pcr():
    '''Muestra los insumos necesarios para el protocolo PCR.'''
    insumos = datos.INSUMOS_PCR

    print()
    print("Insumos del protocolo PCR:")
    print("Protocolo |  Insumo     |     Stock |  Unidad  |   Alerta en")
    print("--------------------------------------------------------------")

    for i in range(len(insumos)):
        print(f"{insumos[i][0]:<11} {insumos[i][1]:<18} {insumos[i][2]:<7} {insumos[i][3]:<11} {insumos[i][4]}")

    alertas = alertar_stock_bajo(insumos)
    if alertas:
        print()
        for alerta in alertas:
            print(alerta)
    else:
        print("\nNo hay insumos con stock menor a 2.")

    return insumos



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
    insumos = datos.INSUMOS_ELECTROFORESIS

    print()
    print("Insumos del protocolo Electroforesis:")
    print("Protocolo   |   Insumo      |      Stock  | Unidad      |   Alerta en")
    print("----------------------------------------------------------------")

    for i in range(len(insumos)):
        print(f"{insumos[i][0]:<15} {insumos[i][1]:<18} {insumos[i][2]:<7} {insumos[i][3]:<11} {insumos[i][4]}")

    alertas = alertar_stock_bajo(insumos)
    if alertas:
        print()
        for alerta in alertas:
            print(alerta)
    else:
        print("\nNo hay insumos con stock menor a 2.")

    return insumos


def mostrar_insumos_extraccion_adn():
    '''Muestra los insumos necesarios para el protocolo Extraccion de ADN.'''
    insumos = datos.INSUMOS_EXTRACCION_ADN

    print()
    print("Insumos del protocolo Extraccion de ADN:")
    print("Protocolo      |    Insumo         |       Stock  | Unidad      |   Alerta en")
    print("-------------------------------------------------------------------------")

    for i in range(len(insumos)):
        print(f"{insumos[i][0]:<20} {insumos[i][1]:<23} {insumos[i][2]:<7} {insumos[i][3]:<11} {insumos[i][4]}")

    alertas = alertar_stock_bajo(insumos)
    if alertas:
        print()
        for alerta in alertas:
            print(alerta)
    else:
        print("\nNo hay insumos con stock menor a 2.")

    return insumos


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

def agregar_stock():
    """
    Proposito: Permite al usuario seleccionar un insumo para agregar stock
    Retorna: No retorna nada, pero actualiza la cantidad del insumo seleccionado.
    """
    print("1. PCR")
    print("2. Electroforesis")
    print("3. Extraccion de ADN")

    grupo_Insumos = pedir_opcion("Seleccione un insumo: ", 1, 3) #Primero se le pide que elija uno de los 3 grupos de insumos
    
    if grupo_Insumos == 1:
        insumos = datos.INSUMOS_PCR
        print("Has seleccionado agregar stock para un insumo del protocolo PCR")
        mostrar_insumos_pcr()
    elif grupo_Insumos == 2:
        insumos = datos.INSUMOS_ELECTROFORESIS
        print("Has seleccionado agregar stock para un insumo del protocolo Electroforesis")
        mostrar_insumos_electroforesis()
    elif grupo_Insumos == 3:
        insumos = datos.INSUMOS_EXTRACCION_ADN
        print("Has seleccionado agregar stock para un insumo del protocolo Extraccion de ADN")
        mostrar_insumos_extraccion_adn()
    
    pedirInsumoEspecifico = pedir_opcion("Seleccione el insumo al que desea agregar stock: ", 1, len(insumos)) #Luego se le pide que elija el insumo especifico de ese grupo de insumos
    insumoSeleccionado = insumos[pedirInsumoEspecifico - 1]
    sumar_stock(insumoSeleccionado) #Se llama a la funcion auxiliar para sumar stock al insumo seleccionado

def sumar_stock(insumo):
    """
    Proposito: Permite al usuario sumar stock a un insumo seleccionado.
    Parametros: insumo (lista): La lista del insumo al que se le va a agregar stock.
    Retorna: No retorna nada, pero actualiza la cantidad del insumo seleccionado.
    """
    cantidadActual = insumo[2]
    cantidadAgregar = int(input(f"Ingrese la cantidad de {insumo[1]} a agregar, 0 para cancelar: "))
    while cantidadAgregar < 0:
        print("Cantidad invalida. Debe ser un numero positivo.")
        cantidadAgregar = int(input(f"Ingrese la cantidad de {insumo[1]} a agregar, 0 para cancelar: "))
    if cantidadAgregar == 0:
        print("No se ha agregado stock.")
        return
    insumo[2] = cantidadActual + cantidadAgregar
    print("Stock actualizado")

def main():
    acceso = False
    while acceso == False:
        usuario_ingresado = input ("Ingrese su nombre de usuario: ")
        contraseña_ingresada = input ("Ingrese su contraseña: ")
        if login (usuario_ingresado, contraseña_ingresada, datos.lista_usuarios, datos.lista_contraseñas):
            acceso = True
            menu()
        else:
            print ("usuario o contraseña incorrectos, intente nuevamente")

main()