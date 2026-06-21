import datos
from funciones_cargapermanente import cargar_datos_insumos, guardar_datos_insumos, cargar_estadisticas_insumos, guardar_estadisticas_insumos, cargar_datos_personal, guardar_datos_personal, agregar_personal, modificar_personal, eliminar_personal
import vistas_protocolos
#funciones para mostrar los insumos y procesos basicos de cada protocolo, y para pedir opciones al usuario en los menus

def pedir_opcion(mensaje, minimo, maximo):
    '''Pide al usuario que ingrese una opcion entre minimo y maximo.'''
    while True:
        try:
            opcion = int(input(mensaje))
        except ValueError:
            print("Debe ingresar un numero valido.")
            continue

        if opcion < minimo or opcion > maximo:
            print(f"Ingrese una opcion entre {minimo} y {maximo}.")
            continue
        return opcion

def pedir_entero_minimo(mensaje, minimo):
    '''Pide al usuario que ingrese un numero entero mayor o igual al minimo.'''
    while True:
        try:
            numero = int(input(mensaje))
        except ValueError:
            print("Debe ingresar un numero valido.")
            continue

        if numero < minimo:
            print(f"Ingrese un numero mayor o igual a {minimo}.")
            continue
        return numero

def obtener_insumos(insumos):
    '''Devuelve los insumos para recorrerlos, aunque esten guardados en un diccionario.'''
    return insumos.values()

def alertar_stock_bajo(insumos):
    '''Genera alertas para los insumos con stock menor o igual a su nivel minimo usando lista por comprension,funcion lambda y filter .'''
    insumos_stock_bajo=list(filter(lambda insumo: insumo["cantidad"] <= insumo["stock_minimo"], obtener_insumos(insumos)))
    return [
        f"Alerta: {insumo['nombre']} tiene {insumo['cantidad']} {insumo['unidad']} disponible(s). Se debe reabastecer."
        for insumo in insumos_stock_bajo
    ]


def solicitar_uso_insumo(nombre_grupo, insumos):
    '''Solicita el insumo a utilizar y la cantidad de stock a descontar.
    Se implemento try-except para manejar errores de ingreso de datos, y se actualiza el stock del insumo seleccionado'''
    print()
    print("Seleccione el insumo que va a utilizar:")
    print()

    for id_insumo, datos_insumo in insumos.items():
        print(f"{id_insumo}. {datos_insumo['nombre']} - Stock disponible: {datos_insumo['cantidad']} {datos_insumo['unidad']}")
        print()

    try:
        id_insumo = input("Ingrese el numero del insumo: ")

        if id_insumo not in insumos:
            raise IndexError

        insumo_seleccionado = insumos[id_insumo]
        
        cantidad_confirmada= False
        while cantidad_confirmada==False:

            cantidad = int(input(f"Ingrese la cantidad de {insumo_seleccionado['nombre']} a utilizar: "))

            while cantidad < 1 or cantidad > insumo_seleccionado["cantidad"]:
                print("Cantidad invalida. Debe ser mayor a 0 y no superar el stock disponible.")
                cantidad = int(input(f"Ingrese la cantidad de {insumo_seleccionado['nombre']} a utilizar: "))
            print()
            print(f"Cantidad de {insumo_seleccionado['nombre']} a utilizar: {cantidad} {insumo_seleccionado['unidad']}")
            confirmacion = input("¿Confirma que desea utilizar esta cantidad? (s/n): ").strip().lower()
            if confirmacion=="s":
                cantidad_confirmada=True
            elif confirmacion=="n":
                print("Operacion cancelada. Por favor, ingrese la cantidad nuevamente.")
            
        

        stock_disponible = insumo_seleccionado["cantidad"]
        stock_restante = stock_disponible - cantidad
        insumo_seleccionado["cantidad"] = stock_restante

        datos_insumos = cargar_datos_insumos()

        datos_estadisticas = cargar_estadisticas_insumos()

        datos_insumos[nombre_grupo][id_insumo]["cantidad"] = stock_restante
        
        datos_estadisticas[nombre_grupo][id_insumo]["cantidad_usada"] += cantidad

        datos_estadisticas["TOTALES"][nombre_grupo] += cantidad

        guardar_datos_insumos(datos_insumos)

        guardar_estadisticas_insumos(datos_estadisticas)

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
            solicitar_uso_insumo("INSUMOS_PCR", insumos)
        elif opcion == 2:
            vistas_protocolos.mostrar_proceso_basico_pcr()
        elif opcion == 3:
            vistas_protocolos.temperatura_protocolo_pcr()
        elif opcion == 4:
            print("Volviendo al menu principal...")
            return
        

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
            solicitar_uso_insumo("INSUMOS_ELECTROFORESIS", insumos)
        elif opcion == 2:
            vistas_protocolos.mostrar_proceso_basico_electroforesis()
        elif opcion == 3:
            vistas_protocolos.temperatura_protocolo_electroforesis()
        elif opcion == 4:
            print("Volviendo al menu principal...")
            return


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
            solicitar_uso_insumo("INSUMOS_EXTRACCION_ADN", insumos)
        elif opcion == 2:
            vistas_protocolos.mostrar_proceso_basico_extraccion_adn()
        elif opcion == 3:
            vistas_protocolos.temperatura_protocolo_extraccion_adn()
        elif opcion == 4:
            print("Volviendo al menu principal...")
            return

def menu_personal():
    """Muestra el menu de gestion del personal del laboratorio."""
    while True:
        print()
        print("Menu del Personal del Laboratorio")
        print("---------------------------------")
        print("1. Consultar datos del personal")
        print("2. Agregar personal")
        print("3. Modificar personal")
        print("4. Eliminar personal")
        print("5. Volver al menu principal")

        try:
            opcion = pedir_opcion("Seleccione una opcion: ", 1, 5)
        except ValueError as e:
            print(e)
            continue

        if opcion == 1:
            import datos_personal
            datos_personal.consultar_dato()
        elif opcion == 2:
            datos_nuevo = {
                "Nombre": input("Nombre: "),
                "Telefono": input("Telefono: "),
                "Direccion": input("Direccion: "),
                "Correo": input("Correo: "),
                "Obra Social": input("Obra Social: "),
                "Estado Civil": input("Estado Civil: "),
                "Edad": input("Edad: "),
            }
            if agregar_personal(datos_nuevo):
                print("Personal agregado con exito.")
        elif opcion == 3:
            if modificar_personal():
                print("Personal modificado con exito.")
        elif opcion == 4:
            nombre_persona = input("Ingrese el nombre de la persona a eliminar: ")
            if eliminar_personal(nombre_persona):
                print("Personal eliminado con exito.")
        elif opcion == 5:
            print("Volviendo al menu principal...")
            return

def menu():
    '''Muestra el menu principal del programa.'''
    dato = 0
    while dato != 10:
        print("***********************************************************************************")
        print("Bienvenido al programa de control de insumos y protocolos de Laboratorios Umbrella")
        print("***********************************************************************************")
        print("1. Protocolo PCR")
        print("2. Protocolo Electroforesis")
        print("3. Protocolo Extraccion de ADN")
        print("4. Agregar stock por protocolo")
        print("5. Agregar stock a todos los protocolos")
        print("6. Mostrar datos de todos los insumos de los protocolos")
        print("7. Gestionar datos del personal del laboratorio")
        print("8. Consultar insumos con igual fecha de vencimiento")
        print("9. Estadisticas")
        print("10. Salir del sistema")
        print()

        try:
            dato = pedir_opcion("Ingrese opcion de protocolo a realizar o otra opcion requerida: ", 1, 10)
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
            print("Has seleccionado gestionar datos del personal del laboratorio")
            menu_personal()
        elif dato == 8:
            print("Has seleccionado consultar insumos con igual fecha de vencimiento")
            insumos_vto_iguales()
        elif dato == 9:
            print("Has seleccionado ver estadisticas")
            calcular_uso_protocolos()
        elif dato == 10:
            print("Has seleccionado salir del sistema")

def mostrar_insumos_pcr():
    """Muestra los insumos necesarios para el protocolo PCR. """
    datos_insumos = cargar_datos_insumos()
    insumos = datos_insumos["INSUMOS_PCR"]

    print()
    print("Insumos del protocolo PCR:")
    print("ID        |  Insumo     |     Stock |  Unidad  |   Alerta en")
    print("--------------------------------------------------------------")

    list(map(lambda insumo: print(f"{insumo[0]:<11} {insumo[1]['nombre']:<18} {insumo[1]['cantidad']:<7} {insumo[1]['unidad']:<11} {insumo[1]['stock_minimo']}"), insumos.items()))

    alertas = alertar_stock_bajo(insumos)
    if alertas:
        print()
        for alerta in alertas:
            print(alerta)
    else:
        print("\nNo hay insumos con stock menor a 2.")

    return insumos


def mostrar_insumos_electroforesis():
    '''Muestra los insumos necesarios para el protocolo Electroforesis.'''
    datos_insumos = cargar_datos_insumos()
    insumos = datos_insumos["INSUMOS_ELECTROFORESIS"]

    print()
    print("Insumos del protocolo Electroforesis:")
    print("ID        |  Insumo     |     Stock |  Unidad  |   Alerta en")
    print("--------------------------------------------------------------")

    list(map(lambda insumo: print(f"{insumo[0]:<11} {insumo[1]['nombre']:<18} {insumo[1]['cantidad']:<7} {insumo[1]['unidad']:<11} {insumo[1]['stock_minimo']}"), insumos.items()))


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
    datos_insumos = cargar_datos_insumos()
    insumos = datos_insumos["INSUMOS_EXTRACCION_ADN"]

    print()
    print("Insumos del protocolo Extraccion de ADN:")
    print("ID        |  Insumo     |     Stock |  Unidad  |   Alerta en")
    print("--------------------------------------------------------------")

    list(map(lambda insumo: print(f"{insumo[0]:<11} {insumo[1]['nombre']:<18} {insumo[1]['cantidad']:<7} {insumo[1]['unidad']:<11} {insumo[1]['stock_minimo']}"), insumos.items()))

    alertas = alertar_stock_bajo(insumos)
    if alertas:
        print()
        for alerta in alertas:
            print(alerta)
    else:
        print("\nNo hay insumos con stock menor a 2.")

    return insumos

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
    datos_insumos = cargar_datos_insumos()

    print("1. PCR")
    print("2. Electroforesis")
    print("3. Extraccion de ADN")

    grupo_Insumos = pedir_opcion("Seleccione un insumo: ", 1, 3) #Primero se le pide que elija uno de los 3 grupos de insumos
    
    if grupo_Insumos == 1:
        nombre_grupo= "INSUMOS_PCR"
        datos_insumos = cargar_datos_insumos()
        insumos = datos_insumos["INSUMOS_PCR"]
        print("Has seleccionado agregar stock para un insumo del protocolo PCR")
        mostrar_insumos_pcr()
    elif grupo_Insumos == 2:
        nombre_grupo= "INSUMOS_ELECTROFORESIS"
        datos_insumos = cargar_datos_insumos()
        insumos = datos_insumos["INSUMOS_ELECTROFORESIS"]
        print("Has seleccionado agregar stock para un insumo del protocolo Electroforesis")
        mostrar_insumos_electroforesis()
    elif grupo_Insumos == 3:
        nombre_grupo= "INSUMOS_EXTRACCION_ADN"
        datos_insumos = cargar_datos_insumos()
        insumos = datos_insumos["INSUMOS_EXTRACCION_ADN"]
        print("Has seleccionado agregar stock para un insumo del protocolo Extraccion de ADN")
        mostrar_insumos_extraccion_adn()
    
    pedirInsumoEspecifico = pedir_opcion("Seleccione el insumo al que desea agregar stock: ", 1, len(insumos)) #Luego se le pide que elija el insumo especifico de ese grupo de insumos
    insumoSeleccionado = insumos[str(pedirInsumoEspecifico)]

    cantidadAgregar = pedir_entero_minimo(f"Ingrese la cantidad de {insumoSeleccionado['nombre']} a agregar, 0 para cancelar: ", 0)
    if cantidadAgregar == 0:
        print("No se ha agregado stock.")
        return
    
    print("Cantidad de stock ingresada")
    sumar_stock(datos_insumos, nombre_grupo, str(pedirInsumoEspecifico), cantidadAgregar) #Se llama a la funcion auxiliar para sumar stock al insumo seleccionado
    guardar_datos_insumos(datos_insumos)


def sumar_stock(datos_insumos, grupo_insumos, id_insumo, stock_a_agregar):
    """
    Proposito: Suma stock a un insumo especifico dentro del archivo datos_insumos.json.
    Parametros:
        datos_insumos: diccionario con los datos de los insumos
        grupo_insumos: nombre del grupo en el JSON, por ejemplo "INSUMOS_PCR"
        id_insumo: clave del insumo dentro del grupo, por ejemplo "1"
        stock_a_agregar: cantidad de stock a sumar
    Retorna: No retorna nada, pero actualiza datos_insumos.json.
    """
    if stock_a_agregar < 0:
        print("No se puede agregar una cantidad negativa de stock.")
        return

    if grupo_insumos not in datos_insumos:
        print("El grupo de insumos no existe.")
        return

    if id_insumo not in datos_insumos[grupo_insumos]:
        print("El insumo seleccionado no existe.")
        return

    datos_insumos[grupo_insumos][id_insumo]["cantidad"] += stock_a_agregar


def agregar_stock_a_grupo():
    """
    Proposito: Permite al usuario sumar stock a un grupo de insumos.
    Obs: Si el usuario selecciona un grupo de insumos, se le va a sumar la misma cantidad a todos los insumos de ese grupo. 
    """ 

    datos_insumos = cargar_datos_insumos()


    print("1. PCR")
    print("2. Electroforesis")
    print("3. Extraccion de ADN")

    opcion = pedir_opcion("Seleccione un grupo de insumos: ",1,3) # Se le pide el grupo de insumos al usuario
    
    if opcion == 1:
        nombre_grupo = "INSUMOS_PCR"
        insumos = datos_insumos["INSUMOS_PCR"]
    elif opcion==2:
        nombre_grupo = "INSUMOS_ELECTROFORESIS"
        insumos = datos_insumos["INSUMOS_ELECTROFORESIS"]
    elif opcion==3:
        nombre_grupo = "INSUMOS_EXTRACCION_ADN"
        insumos = datos_insumos["INSUMOS_EXTRACCION_ADN"]

    agregar = pedir_entero_minimo("Ingrese el numero de stock a sumar al grupo: ", 1) # Se le pide la cantidad de stock a sumar al usuario

    for id_insumo in insumos:
        sumar_stock(datos_insumos, nombre_grupo, id_insumo, agregar) # Se llama a la funcion auxiliar para sumar stock a cada insumo del grupo seleccionado

    guardar_datos_insumos(datos_insumos)

    print("Cantidad de stock ingresada")



def insumos_vto_iguales():
    """
    Proposito: Devuelve una lista de insumos con la misma fecha de vencimiento. 
    """

    pcr_vto = datos.fechas_de_vencimiento_pcr()
    adn_vto = datos.fechas_de_vencimiento_adn()
    electro_vto = datos.fechas_de_vencimiento_electrofosis()

    comunes = pcr_vto & adn_vto & electro_vto
      
    for fecha in comunes:
        anio,mes,dia=fecha.split("-")
        fecha_prolija=(f"{dia}/{mes}/{anio}")
        
        insumos = (datos.buscar_insumos_por_fecha(fecha))
        print(f"\nInsumos con Fecha de vencimiento en comun: {fecha_prolija}")
        print("--------------------------------------------")
        print("                Insumos:                   ")
        print("--------------------------------------------")
        for insumos in insumos: 
            print(f"|  - {insumos:<35}|")
        print("--------------------------------------------")
        
    print("1. Volver al menu principal")

    opcion = input("Seleccione una opcion: ")

    if(opcion == "1"):
        print("Volviendo al menu principal...")
    


def calcular_uso_protocolos():
    """
    Proposito: Calcula el uso total de cada insumo en cada protocolo y lo muestra en consola.
    Salida: Imprime en consola el uso total de cada insumo en cada protocolo.
    """
    datos_estadisticas = cargar_estadisticas_insumos()

    if not datos_estadisticas:
        print("No hay registros estadísticos acumulados en el archivo.")
        return

    totales_protocolos = datos_estadisticas["TOTALES"]

    total_general = sum(totales_protocolos.values())

    print("Estadisticas de uso de insumos por protocolo:")
    if total_general == 0:
        print("Aún no se han registrado consumos.")
        return

    for protocolo, total_usado in totales_protocolos.items():
        porcentaje = (total_usado / total_general) * 100
        print(f"Protocolo {protocolo}: {porcentaje:.2f}% (Total unidades utilizadas: {total_usado})")
    
    pcr = totales_protocolos.get("INSUMOS_PCR", 0)
    electro = totales_protocolos.get("INSUMOS_ELECTROFORESIS", 0)
    adn = totales_protocolos.get("INSUMOS_EXTRACCION_ADN", 0)
    
    if pcr > electro and pcr > adn:
        print("El protocolo PCR es el más utilizado.")
    elif electro > pcr and electro > adn:
        print("El protocolo Electroforesis es el más utilizado.")
    elif adn > pcr and adn > electro:
        print("El protocolo Extraccion de ADN es el más utilizado.")
    else:
        print("Todos los protocolos tienen el mismo uso")

    print("1. Volver al menu principal")
    opcion = input("Seleccione una opcion: ")

    if opcion == "1":
        print("Volviendo al menu principal...")
