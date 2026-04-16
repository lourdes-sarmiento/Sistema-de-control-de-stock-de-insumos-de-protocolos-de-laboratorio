#Aquí reciden los datos de los usuarios y los insumos para cada proceso, con sus cantidades y unidades correspondientes.
#Usuarios y contraseñas para el login
#bonjour desde el github de valen
lista_usuarios = ["carlos" , "javier"] 
lista_contraseñas = ["1" , "2"]

#Insumos numerados 
INSUMOS_PCR = [
    ["1", "Primers", 6, "unidades", "<= 2"],
    ["2", "dNTPs", 5, "unidades", "<= 2"],
    ["3", "ADN Polimerasa", 1, "frascos", "<= 2"],
    ["4", "Cofactor", 5, "unidades", "<= 2"],
    ["5", "Buffer de PCR", 6, "frascos", "<= 2"],
    ["6", "Tubos de PCR", 10, "unidades", "<= 2"]
]

INSUMOS_ELECTROFORESIS = [
    ["1", "Gel de agarosa", 6, "frascos", "<= 2"],
    ["2", "Buffer de corrida", 8, "frascos", "<= 2"],
    ["3", "Agente intercalante", 1, "frascos", "<= 2"],
    ["4", "Marcador peso mol.", 1, "unidades", "<= 2"]
]

INSUMOS_EXTRACCION_ADN = [
    ["1", "Buffer de lisis", 7, "frascos", "<= 2"],
    ["2", "Enzimas", 6, "frascos", "<= 2"],
    ["3", "Agentes de separacion", 4, "frascos", "<= 2"],
    ["4", "Alcoholes", 5, "frascos", "<= 2"],
    ["5", "Buffer de elucion", 1, "frascos", "<= 2"]
]
