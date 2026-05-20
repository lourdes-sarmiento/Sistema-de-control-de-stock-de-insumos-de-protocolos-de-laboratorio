#Aquí reciden los datos de los usuarios y los insumos para cada proceso, con sus cantidades y unidades correspondientes.
#Usuarios y contraseñas para el login

usuarios = {  #La clave es el nombre del usuario (clave primaria) y el valor es su contraseña, la cual puede repetirse. 
    "carlos": "1",
    "javier": "2"
}

lista_usuarios = list(usuarios.keys())
lista_contraseñas = list(usuarios.values())

#Los insumos ahora se dividen en diccionarios tales que:
#Su clave es el numero de id del grupo de insumos y su valor es un diccionario el cual tiene las caracteristicas de ese insumo.

INSUMOS_PCR = { 
    "1": {
        "nombre": "Primers",
        "cantidad": 6,
        "unidad": "unidades",
        "stock_minimo": 1,
        "vencimiento": "2026-12-15"
    },
    "2": {
        "nombre": "dNTPs",
        "cantidad": 5,
        "unidad": "unidades",
        "stock_minimo": 2,
        "vencimiento": "2026-08-20"
    },
    "3": {
        "nombre": "ADN Polimerasa",
        "cantidad": 1,
        "unidad": "frascos",
        "stock_minimo": 2,
        "vencimiento": "2026-06-01"
    },
    "4": {
        "nombre": "Cofactor",
        "cantidad": 5,
        "unidad": "unidades",
        "stock_minimo": 2,
        "vencimiento": "2027-01-10"
    },
    "5": {
        "nombre": "Buffer de PCR",
        "cantidad": 6,
        "unidad": "frascos",
        "stock_minimo": 2,
        "vencimiento": "2026-11-30"
    },
    "6": {
        "nombre": "Tubos de PCR",
        "cantidad": 10,
        "unidad": "unidades",
        "stock_minimo": 2,
        "vencimiento": "2028-05-01"
    }
}

INSUMOS_ELECTROFORESIS = {
    "1": {
        "nombre": "Gel de agarosa",
        "cantidad": 6,
        "unidad": "frascos",
        "stock_minimo": 2,
        "vencimiento": "2026-11-30"
    },
    "2": {
        "nombre": "Buffer de corrida",
        "cantidad": 8,
        "unidad": "frascos",
        "stock_minimo": 2,
        "vencimiento": "2026-10-12"
    },
    "3": {
        "nombre": "Agente intercalante",
        "cantidad": 1,
        "unidad": "frascos",
        "stock_minimo": 2,
        "vencimiento": "2026-07-05"
    },
    "4": {
        "nombre": "Marcador peso mol.",
        "cantidad": 1,
        "unidad": "unidades",
        "stock_minimo": 2,
        "vencimiento": "2026-09-22"
    }
}

INSUMOS_EXTRACCION_ADN = {
    "1": {
        "nombre": "Buffer de lisis",
        "cantidad": 7,
        "unidad": "frascos",
        "stock_minimo": 2,
        "vencimiento": "2026-11-30"
    },
    "2": {
        "nombre": "Enzimas",
        "cantidad": 6,
        "unidad": "frascos",
        "stock_minimo": 2,
        "vencimiento": "2026-06-15"
    },
    "3": {
        "nombre": "Agentes de separacion",
        "cantidad": 4,
        "unidad": "frascos",
        "stock_minimo": 2,
        "vencimiento": "2027-02-28"
    },
    "4": {
        "nombre": "Alcoholes",
        "cantidad": 5,
        "unidad": "frascos",
        "stock_minimo": 2,
        "vencimiento": "2027-12-31"
    },
    "5": {
        "nombre": "Buffer de elucion",
        "cantidad": 1,
        "unidad": "frascos",
        "stock_minimo": 2,
        "vencimiento": "2026-08-14"
    }
}

def fechas_de_vencimiento_pcr():
    """
    Proposito: Devuelve un conjunto de fechas de vencimiento de los insumos de PCR.
    Salida: Un conjunto de fechas de vencimiento de los insumos de PCR.
    """
    fechas_pcr = set()
    
    for i in INSUMOS_PCR.values(): 
        fechas_pcr.add(i["vencimiento"])
    return fechas_pcr
    

def fechas_de_vencimiento_adn():
    """
    Proposito: Devuelve un conjunto de fechas de vencimiento de los insumos de Extraccion de ADN.
    Salida: Un conjunto de fechas de vencimiento de los insumos de Extraccion de ADN.
    """
    fechas_adn = set()
    for i in INSUMOS_EXTRACCION_ADN.values():
        fechas_adn.add(i["vencimiento"])
    return fechas_adn

def fechas_de_vencimiento_electrofosis():
    """
    Proposito: Devuelve un conjunto de fechas de vencimiento de los insumos de Electrofosis.
    Salida: Un conjunto de fechas de vencimiento de los insumos de Electrofosis.
    """
    fechas_electro = set()
    for i in INSUMOS_ELECTROFORESIS.values():
        fechas_electro.add(i.get("vencimiento"))
    return fechas_electro

def buscar_insumos_por_fecha(fecha):
    """
    Proposito: Devuelve una lista de insumos que vencen en la fecha dada.
    Parametros: fecha (str): La fecha de vencimiento a buscar en formato "YYYY-MM-DD".
    Salida: Una lista de insumos que vencen en la fecha dada.
    """
    insumos = []
    
    for insumo in INSUMOS_PCR.values():
        if insumo["vencimiento"] == fecha:
            insumos.append(insumo["nombre"])
    
    for insumo in INSUMOS_ELECTROFORESIS.values():
        if insumo["vencimiento"] == fecha:
            insumos.append(insumo["nombre"])
    
    for insumo in INSUMOS_EXTRACCION_ADN.values():
        if insumo["vencimiento"] == fecha:
            insumos.append(insumo["nombre"])
    
    return insumos
