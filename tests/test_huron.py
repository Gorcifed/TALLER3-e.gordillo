import unittest
from models.huron import Huron

class TestHuron(unittest.TestCase):
    _huron = Huron("Pepe", 5, 2.5, "Guatemala", 52.23)
    def test_hacer_sonido(self):
        self.assertEqual(self._huron.hacer_sonido(), "¡Eek Eek!")

    def test_calcular_flete(self):
        self.assertEqual(self._huron.impuestos, 52.23)

if __name__ == '__main__':
    unittest.main()