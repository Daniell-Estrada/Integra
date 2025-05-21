import unittest
from unittest.mock import MagicMock

from comida.menu import Plato
from comida.restaurante import Restaurante


class TestRestaurante(unittest.TestCase):
    """Pruebas unitarias para la clase Pedido."""

    def setUp(self):
        """Configura un pedido y un plato para cada prueba."""
        self.plato = Plato("Ensalada", 5.0)
        self.pedido = MagicMock()
        self.menu = MagicMock()
        self.restaurante = Restaurante(self.menu)
        

    def test_agregar_plato(self):
        """Verifica que se pueda agregar un plato al pedido."""
        self.menu.obtener_plato.return_value = True # Simula que el plato existe en el menú
        salida = self.restaurante.agregar_plato_a_pedido(self.pedido, self.plato.nombre) 
        self.assertTrue(salida)
        
if __name__ == "__main__":
    unittest.main()
