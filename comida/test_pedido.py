import unittest
from unittest.mock import MagicMock

from restaurante import Pedido


class TestPedido(unittest.TestCase):
    """Pruebas unitarias para la clase Pedido."""

    def setUp(self):
        """Configura un pedido y un plato para cada prueba."""
        self.pedido = Pedido()
        self.plato_mock = MagicMock()
        self.plato_mock.precio = 10.0
        self.pedido.agregar_plato(self.plato_mock)

    def test_agregar_plato(self):
        """Verifica que se pueda agregar un plato al pedido."""
        self.assertIn(self.plato_mock, self.pedido.platos)

    def test_calcular_total(self):
        """Verifica que el total del pedido se calcule correctamente."""
        total = self.pedido.calcular_total()
        self.assertEqual(total, 10.0)


if __name__ == "__main__":
    unittest.main()
