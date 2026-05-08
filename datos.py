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

pcr = { 
    "1": {
        "nombre":"Primers",
        "cantidad": 6,
        "unidad": "unidades",
        "minimo": 1},
    "2": {
        "nombre":"dNTPs",
        "cantidad":5,
        "unidad" : "unidades",
        "minimo" : 2},
    "3": {
        "nombre" : "ADN Polimerasa",
        "cantidad" : 1,
        "unidad" : "frascos",
        "minimo" : 2},
    "4": {
        "nombre" : "Cofactor",
        "cantidad" : 5,
        "unidad" : "unidades",
        "minimo" : 2},
    "5": {
        "nombre" : "Buffer de PCR",
        "cantidad" : 6,
        "unidad" : "frascos",
        "minimo" : 2},
    "6": {
        "nombre" : "Tubos de PCR",
        "cantidad" : 10,
        "unidad" : "unidades",
        "minimo" : 2}
    }


electrofosis = {
    "1": {
        "nombre":"Gel de agarosa",
        "cantidad": 6,
        "unidad": "frascos",
        "minimo": 2},
    "2": {
        "nombre":"Buffer de corrida",
        "cantidad": 8,
        "unidad": "frascos",
        "minimo": 2},
    "3": {
        "nombre":"Agente intercalante",
        "cantidad": 1,
        "unidad":"frascos",
        "minimo": 2},
    "4": {
        "nombre":"Marcador peso mol.",
        "cantidad": 1,
        "unidad":"unidades",
        "minimo": 2}
    }



extraccion_adn = {
    "1": {
        "nombre":"Buffer de lisis",
        "cantidad": 7,
        "unidad": "frascos",
        "minimo": 2},
    "2": {
        "nombre":"Enzimas",
        "cantidad": 6,
        "unidad": "frascos",
        "minimo": 2},
    "3": {
        "nombre":"Agentes de separacion",
        "cantidad": 4,
        "unidad":"frascos",
        "minimo": 2},
    "4": {
        "nombre":"Alcoholes",
        "cantidad": 5,
        "unidad":"frascos",
        "minimo": 2},
    "5": {
        "nombre":"Buffer de elucion",
        "cantidad": 1,
        "unidad":"frascos",
        "minimo": 2}
    }
