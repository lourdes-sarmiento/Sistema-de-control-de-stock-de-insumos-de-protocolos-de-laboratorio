import datos

#funciones para mostrar los insumos y procesos basicos de cada protocolo, y para pedir opciones al usuario en los menus

def pedir_opcion(mensaje, minimo, maximo):
    '''Pide al usuario que ingrese una opcion entre minimo y maximo.'''
    while True:
        try:
            opcion = int(input(mensaje))
        except ValueError:
            raise ValueError("Debe ingresar un número válido.")

        if opcion < minimo or opcion > maximo:
            print(f"Ingrese una opcion entre {minimo} y {maximo}.")
            continue
        return opcion

def obtener_insumos(insumos):
    '''Devuelve los insumos para recorrerlos, aunque esten guardados en un diccionario.'''
    return insumos.values()

def alertar_stock_bajo(insumos):
    '''Genera alertas para los insumos con stock menor o igual a su nivel minimo usando lista por comprension,funcion lambda y filter .'''
    insumos_stock_bajo=list(filter(lambda insumo: insumo["cantidad"] <= insumo["stock_minimo"], obtener_insumos(insumos)))
    return [
        f"Alerta: {insumo["nombre"]} tiene {insumo["cantidad"]} {insumo["unidad"]} disponible(s). Se debe reabastecer."
        for insumo in insumos_stock_bajo
    ]


def solicitar_uso_insumo(insumos):
    '''Solicita el insumo a utilizar y la cantidad de stock a descontar. 
    Se implemento try-except para manejar errores de ingreso de datos, y se actualiza el stock del insumo seleccionado'''
    print()
    print("Seleccione el insumo que va a utilizar:")
    print()

    for id_insumo, datos_insumo in insumos.items():
        print(f"{id_insumo}. {datos_insumo['nombre']} - Stock disponible: {datos_insumo['cantidad']} {datos_insumo['unidad']}")
        print()

    lista_insumos = list(insumos.values())

    try:
        opcion_insumo = int(input("Ingrese el numero del insumo: "))

        if opcion_insumo < 1:
            raise IndexError

        insumo_seleccionado = lista_insumos[opcion_insumo - 1]

        cantidad = int(input(f"Ingrese la cantidad de {insumo_seleccionado['nombre']} a utilizar: "))

        while cantidad < 1 or cantidad > insumo_seleccionado["cantidad"]:
            print("Cantidad invalida. Debe ser mayor a 0 y no superar el stock disponible.")
            cantidad = int(input(f"Ingrese la cantidad de {insumo_seleccionado['nombre']} a utilizar: "))

        stock_disponible = insumo_seleccionado["cantidad"]
        stock_restante = stock_disponible - cantidad
        insumo_seleccionado["cantidad"] = stock_restante

        print()
        print(f"Insumo seleccionado: {insumo_seleccionado['nombre']}")
        print(f"Stock disponible: {stock_disponible} {insumo_seleccionado['unidad']}")
        print(f"Cantidad a utilizar: {cantidad} {insumo_seleccionado['unidad']}")
        print(f"Stock restante: {stock_restante} {insumo_seleccionado['unidad']}")

        alertar_stock_bajo(insumos)

    except ValueError:
        print("Error: debe ingresar un numero valido numerico.")
    except IndexError:
        print("Error: el insumo seleccionado no existe.")

def temperatura_protocolo_pcr(): 
    '''Muestra la temperatura de cada etapa del protocolo PCR utilizando tuplas.'''
    print()
    print("Temperaturas del protocolo PCR:")
    pcr=(
        ("Desnaturalizacion",94,98),
        ("Alineamiento",55,60),
        ("Extension",72,75)
    )
    for proceso,temp_min,temp_max in pcr:
        print(f"{proceso}: entre {temp_min}°C y {temp_max}°C")


def menu_pcr():
    '''Muestra el menu del protocolo PCR.'''
    while True:
        print()
        print("Menu del Protocolo PCR")
        print("------------------------")
        print("1. Ver insumos y cantidades")#seleccione el insumo luego seleccione la cantidad a utilizar.
        print("2. Ver proceso basico") 
        print("3. Ver temperatura del protocolo")
        print("4. Volver al menu principal")

        try:
            opcion = pedir_opcion("Seleccione una opcion: ", 1, 4)
        except ValueError as e:
            print(e)
            continue

        if opcion == 1:
            insumos = mostrar_insumos_pcr()
            solicitar_uso_insumo(insumos)
        elif opcion == 2:
            mostrar_proceso_basico_pcr()
        elif opcion == 3:
            temperatura_protocolo_pcr()
        elif opcion == 4:
            print("Volviendo al menu principal...")
            break
        
def temperatura_protocolo_electroforesis():
    """Muestra la temperatura de cada etapa del protocolo Electroforesis utilizando tuplas."""
    print()
    print("temperaturas del protocolo Electroforesis:")
    electroforesis=(
        ("preparacion del gel",55),
        ("Corrida del ADN",25),
        ("Recuperacion del ADN",65)
    )            
    for proceso,temperatura in electroforesis:
        print(f"{proceso}: {temperatura}°C")


def menu_electroforesis():
    '''Muestra el menu del protocolo Electroforesis.'''
    while True:
        print()
        print("Menu del Protocolo Electroforesis")
        print("---------------------------------")
        print("1. Ver insumos y cantidades")
        print("2. Ver proceso basico")
        print("3. Ver temperatura del protocolo")
        print("4. Volver al menu principal")

        try:
            opcion = pedir_opcion("Seleccione una opcion: ", 1, 4)
        except ValueError as e:
            print(e)
            continue
        
        if opcion == 1:
            insumos = mostrar_insumos_electroforesis()
            solicitar_uso_insumo(insumos)
        elif opcion == 2:
            mostrar_proceso_basico_electroforesis()
        elif opcion == 3:
            temperatura_protocolo_electroforesis()
        elif opcion == 4:
            print("Volviendo al menu principal...")
            break

def temperatura_protocolo_extraccion_adn():
    '''Muestra la temperatura de cada etapa del protocolo Extraccion de ADN utilizando tuplas.'''
    print()
    print("Temperaturas del protocolo Extraccion de ADN:")
    extraccion_adn=(
        ("Lisis celular",55,65),
        ("Precipitacion",0,-20),
        ("Recuperacion del ADN",-20,-80)
    )
    for proceso,temp_min,temp_max in extraccion_adn:
        print(f"{proceso}: entre {temp_min}°C y {temp_max}°C")


def menu_extraccion_adn():
    '''Muestra el menu del protocolo Extraccion de ADN.'''
    while True:
        print()
        print("Menu del Protocolo Extraccion de ADN")
        print("-------------------------------------")
        print("1. Ver insumos y cantidades")
        print("2. Ver proceso basico")
        print("3. Ver temperatura del protocolo")
        print("4. Volver al menu principal")
        

        try:
            opcion = pedir_opcion("Seleccione una opcion: ", 1, 4)
        except ValueError as e:
            print(e)
            continue

        if opcion == 1:
            insumos = mostrar_insumos_extraccion_adn()
            solicitar_uso_insumo(insumos)
        elif opcion == 2:
            mostrar_proceso_basico_extraccion_adn()
        elif opcion == 3:
            temperatura_protocolo_extraccion_adn()
        elif opcion == 4:
            print("Volviendo al menu principal...")
            break


def menu():
    '''Muestra el menu principal del programa.'''
    dato = 0
    while dato != 9:
        print("***********************************************************************************")
        print("Bienvenido al programa de control de insumos y protocolos de Laboratorios Umbrella")
        print("***********************************************************************************")
        print("1. Protocolo PCR")
        print("2. Protocolo Electroforesis")
        print("3. Protocolo Extraccion de ADN")
        print("4. Agregar stock por protocolo")
        print("5. Agregar stock a todos los protocolos")
        print("6. Mostrar datos de todos los insumos de los protocolos")
        print("7. Consultar datos del personal del laboratorio")
        print("8. Consultar insumos con igual fecha de vencimiento")
        print("9. Salir del sistema")
        print()

        try:
            dato = pedir_opcion("Ingrese opcion de protocolo a realizar: ", 1, 9)
        except ValueError as e:
            print(e)
            continue

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
            print("Has seleccionado agregarle stock a un grupo completo de insumos")
            agregar_stock_a_grupo()
        elif dato == 6:
            print("Has seleccionado ver todo el stock")
            mostrar_datos()
        elif dato == 7:
            print("Has seleccionado consultar datos del personal del laboratorio")
            import datos_personal
            datos_personal.consultar_dato()
        elif dato == 8:
            print("Has seleccionado consultar insumos con igual fecha de vencimiento")
            insumos_vto_iguales()
        elif dato == 9:
            print("Has seleccionado salir del sistema")

def mostrar_insumos_pcr():
    """Muestra los insumos necesarios para el protocolo PCR. """
    insumos = datos.INSUMOS_PCR

    print()
    print("Insumos del protocolo PCR:")
    print("Protocolo |  Insumo     |     Stock |  Unidad  |   Alerta en")
    print("--------------------------------------------------------------")

    list(map(lambda insumo: print(f"{insumo[0]:<11} {insumo[1]["nombre"]:<18} {insumo[1]["cantidad"]:<7} {insumo[1]["unidad"]:<11} {insumo[1]["stock_minimo"]}"), insumos.items()))

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
    print("Protocolo |  Insumo     |     Stock |  Unidad  |   Alerta en")
    print("--------------------------------------------------------------")

    list(map(lambda insumo: print(f"{insumo[0]:<11} {insumo[1]["nombre"]:<18} {insumo[1]["cantidad"]:<7} {insumo[1]["unidad"]:<11} {insumo[1]["stock_minimo"]}"), insumos.items()))


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
    print("Protocolo |  Insumo     |     Stock |  Unidad  |   Alerta en")
    print("--------------------------------------------------------------")

    list(map(lambda insumo: print(f"{insumo[0]:<11} {insumo[1]["nombre"]:<18} {insumo[1]["cantidad"]:<7} {insumo[1]["unidad"]:<11} {insumo[1]["stock_minimo"]}"), insumos.items()))

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

def mostrar_datos():
    """
    Proposito: Imprime todos los datos de todos los insumos
    """
    mostrar_insumos_pcr()
    mostrar_insumos_electroforesis()
    mostrar_insumos_extraccion_adn()

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
    insumoSeleccionado = insumos[str(pedirInsumoEspecifico)]

    cantidadAgregar = int(input(f"Ingrese la cantidad de {insumoSeleccionado["nombre"]} a agregar, 0 para cancelar: "))

    while cantidadAgregar < 0:
        print("Cantidad invalida. Debe ser un numero positivo.")
        cantidadAgregar = int(input(f"Ingrese la cantidad de {insumoSeleccionado["nombre"]} a agregar, 0 para cancelar: "))
    if cantidadAgregar == 0:
        print("No se ha agregado stock.")
        return
    
    print("Cantidad de stock ingresada")
    sumar_stock(insumoSeleccionado,cantidadAgregar) #Se llama a la funcion auxiliar para sumar stock al insumo seleccionado


def sumar_stock(insumo,stock_a_agregar):
    """
    Proposito: Suma el stock de un determinado insumo.
    Parametros: insumo (lista): La lista del insumo al que se le va a agregar stock. stock_a_agregar: Int
    Retorna: No retorna nada, pero actualiza la cantidad del insumo seleccionado.
    """
    insumo["cantidad"] += stock_a_agregar

def agregar_stock_a_grupo():
    """
    Proposito: Permite al usuario sumar stock a un grupo de insumos.
    Obs: Si el usuario selecciona un grupo de insumos, se le va a sumar la misma cantidad a todos los insumos de ese grupo. 
    """ 
    print("1. PCR")
    print("2. Electroforesis")
    print("3. Extraccion de ADN")

    opcion = pedir_opcion("Seleccione un grupo de insumos: ",1,3) # Se le pide el grupo de insumos al usuario
    
    if opcion == 1:
        insumos = datos.INSUMOS_PCR
    elif opcion==2:
        insumos = datos.INSUMOS_ELECTROFORESIS
    elif opcion==3:
        insumos = datos.INSUMOS_EXTRACCION_ADN
    
    while opcion > 4 or opcion < 0:
        opcion = pedir_opcion("Seleccione un grupo de insumos: ",1,3)
    
    agregar = int(input("Ingrese el numero de stock a sumar al grupo: ")) # Se le pide la cantidad de stock a sumar al usuario
 
    while agregar <= 0 : 
        agregar = int(input("Ingrese el numero de stock a sumar al grupo: "))
        print("Cantidad invalida")

    list(map(lambda insumo: sumar_stock(insumo,agregar),insumos.values())) 

    print("Cantidad de stock ingresada")


def insumos_vto_iguales():
    """
    Proposito: Devuelve una lista de insumos con la misma fecha de vencimiento. 
    """

    pcr_vto = datos.fechas_de_vencimiento_pcr()
    adn_vto = datos.fechas_de_vencimiento_adn()
    electro_vto = datos.fechas_de_vencimiento_electrofosis()

    comunes = pcr_vto & adn_vto & electro_vto
    print("Fechas de vencimiento comunes:", comunes)
    for i in comunes:
        insumos = (datos.buscar_insumos_por_fecha(i))
    
    for i in insumos: 
        print(f"Insumos con fecha de vencimiento: {i}")
        
    print("1. Volver al menu principal")

    opcion = input("Seleccione una opcion: ")

    if(opcion == 1):
        print("Volviendo al menu principal...")
    
