import unittest
from modulo1 import sumar_stock
"""
def sumar_stock(insumo, stock_a_agregar):
    'Suma el stock de un determinado insumo.'
    insumo["cantidad"] += stock_a_agregar
"""
class TestSumarStock(unittest.TestCase): #Clase de test para la función sumar_stock

    def test_sumar_stock_feliz(self):
        """
        En este escenario se prueba la funcion de sumar_stock con un insumos y una cantidad validas. Debe sumar correctamente los valores.
        """
        insumo = {"nombre": "Reactivo A", "cantidad": 10}
        
        sumar_stock(insumo, 5)

        self.assertEqual(insumo["cantidad"], 15)

    def test_sumar_stock_cantidad_negativa(self):
        """
        En este escenario se prueba la funcion de sumar_stock con una cantidad negativa, lo cual no deberia modificar el stock del insumo.
        """
        insumo = {"nombre": "Reactivo B", "cantidad": 20}
        
        sumar_stock(insumo, -5)

        self.assertEqual(insumo["cantidad"], 20)

    def test_sumar_stock_cantidad_cero(self):
        """
        En este escenario se prueba la funcion de sumar_stock con una cantidad de cero, lo cual no deberia modificar el stock del insumo.
        """
        insumo = {"nombre": "Reactivo C", "cantidad": 15}
        
        sumar_stock(insumo, 0)

        self.assertEqual(insumo["cantidad"], 15) 

if __name__ == '__main__': # Para ejecutar los tests al correr el script
    unittest.main()
