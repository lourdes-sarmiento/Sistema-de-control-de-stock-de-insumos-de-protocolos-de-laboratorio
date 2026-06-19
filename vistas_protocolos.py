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

def mostrar_proceso_basico_pcr():
    '''Muestra el proceso basico del protocolo PCR.'''
    print()
    print("Proceso basico del protocolo PCR:")
    print("1. Preparar la mezcla de reaccion.")
    print("2. Colocar los tubos en el termociclador.")
    print("3. Configurar los ciclos de desnaturalizacion, alineamiento y extension.")
    print("4. Esperar la finalizacion del proceso.")
    print("5. Conservar el producto para su analisis.")


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