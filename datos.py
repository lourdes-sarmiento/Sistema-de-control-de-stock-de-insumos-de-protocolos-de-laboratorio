usuarios = {  #La clave es el nombre del usuario (clave primaria) y el valor es su contraseña, la cual puede repetirse. 
    "carlos": "1",
    "javier": "2"
}

lista_usuarios = list(usuarios.keys())
lista_contraseñas = list(usuarios.values())
#Operaciones para conjuntos
def fechas_de_vencimiento_pcr(datos_insumos):
    """
    Proposito: Devuelve un conjunto de fechas de vencimiento de los insumos de PCR.
    """
    fechas_pcr = set()
    insumos_pcr = datos_insumos.get("INSUMOS_PCR", {})
    
    for i in insumos_pcr.values(): 
        fechas_pcr.add(i["vencimiento"])
    return fechas_pcr
    

def fechas_de_vencimiento_adn(datos_insumos):
    """
    Proposito: Devuelve un conjunto de fechas de vencimiento de los insumos de Extraccion de ADN.
    Salida: Un conjunto de fechas de vencimiento de los insumos de Extraccion de ADN.
    """
    fechas_adn = set()
    insumos_adn = datos_insumos.get("INSUMOS_EXTRACCION_ADN", {})
    
    for i in insumos_adn.values():
        fechas_adn.add(i["vencimiento"])
    return fechas_adn

def fechas_de_vencimiento_electrofosis(datos_insumos):
    """
    Proposito: Devuelve un conjunto de fechas de vencimiento de los insumos de Electrofosis.
    Salida: Un conjunto de fechas de vencimiento de los insumos de Electrofosis.
    """
    fechas_electro = set()
    insumos_electro = datos_insumos.get("INSUMOS_ELECTROFORESIS", {})
    for i in insumos_electro.values():
        fechas_electro.add(i.get("vencimiento"))
    return fechas_electro

def buscar_insumos_por_fecha(datos_insumos,fecha):
    """
    Proposito: Devuelve una lista de insumos que vencen en la fecha dada.
    Parametros: fecha (str): La fecha de vencimiento a buscar en formato "YYYY-MM-DD".
    Salida: Una lista de insumos que vencen en la fecha dada.
    """
    insumos = []
    
    for categoria in datos_insumos.values():
        for insumo in categoria.values():
            if insumo.get("vencimiento") == fecha:
                insumos.append(insumo["nombre"])
                
    return insumos
