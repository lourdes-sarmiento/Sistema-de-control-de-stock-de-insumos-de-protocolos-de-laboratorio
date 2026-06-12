import unittest
from unittest.mock import patch
from modulo1 import sumar_stock
"""
def sumar_stock(grupo_insumos, id_insumo, stock_a_agregar):
    Proposito: Suma stock a un insumo especifico dentro del archivo datos_insumos.json.
    Parametros:
        grupo_insumos: nombre del grupo en el JSON, por ejemplo "INSUMOS_PCR"
        id_insumo: clave del insumo dentro del grupo, por ejemplo "1"
        stock_a_agregar: cantidad de stock a sumar
    Retorna: No retorna nada, pero actualiza datos_insumos.json.
    if stock_a_agregar < 0:
        print("No se puede agregar una cantidad negativa de stock.")
        return

    datos_insumos = cargar_datos_insumos()

    if grupo_insumos not in datos_insumos:
        print("El grupo de insumos no existe.")
        return

    if id_insumo not in datos_insumos[grupo_insumos]:
        print("El insumo seleccionado no existe.")
        return

    datos_insumos[grupo_insumos][id_insumo]["cantidad"] += stock_a_agregar

    guardar_datos_insumos(datos_insumos)
"""
class TestSumarStock(unittest.TestCase):
    def test_sumar_stock_exitoso(self):
        diccionario_prueba = {
            "INSUMOS_PCR": {
                "1": {"nombre": "Primers", "cantidad": 2}
            }
        }
        
        sumar_stock(diccionario_prueba, "INSUMOS_PCR", "1", 5)
        
        self.assertEqual(diccionario_prueba["INSUMOS_PCR"]["1"]["cantidad"], 7)

    def test_sumar_stock_cantidad_negativa(self):
        diccionario_prueba = {
            "INSUMOS_PCR": {
                "1": {"nombre": "Primers", "cantidad": 2}
            }
        }
        
        sumar_stock(diccionario_prueba, "INSUMOS_PCR", "1", -3)
        
        self.assertEqual(diccionario_prueba["INSUMOS_PCR"]["1"]["cantidad"], 2)

    def test_sumar_stock_grupo_inexistente(self):
        diccionario_prueba = {
            "INSUMOS_PCR": {
                "1": {"nombre": "Primers", "cantidad": 2}
            }
        }
        
        sumar_stock(diccionario_prueba, "INSUMOS_ELECTROFORESIS", "1", 5)
        
        self.assertNotIn("INSUMOS_ELECTROFORESIS", diccionario_prueba)

    def test_sumar_stock_insumo_inexistente(self):
        diccionario_prueba = {
            "INSUMOS_PCR": {
                "1": {"nombre": "Primers", "cantidad": 2}
            }
        }
        
        sumar_stock(diccionario_prueba, "INSUMOS_PCR", "2", 5)
        
        self.assertNotIn("2", diccionario_prueba["INSUMOS_PCR"])

    def test_sumar_stock_cantidad_cero(self):
        diccionario_prueba = {
            "INSUMOS_PCR": {
                "1": {"nombre": "Primers", "cantidad": 2}
            }
        }
        
        sumar_stock(diccionario_prueba, "INSUMOS_PCR", "1", 0)
        
        self.assertEqual(diccionario_prueba["INSUMOS_PCR"]["1"]["cantidad"], 2)

    

if __name__ == '__main__': # Para ejecutar poner python test_sumar_stock.py en la terminal
    unittest.main()
