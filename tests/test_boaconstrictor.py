import unittest
from models.boaConstrictor import BoaConstrictor

class TestBoa(unittest.TestCase):
    _boa1 = BoaConstrictor("Margarita", 5, 2.0,"Colombia",20.2)
    def test_hacer_sonido(self):
        self.assertEqual(self._boa1.hacer_sonido(), "¡Tsss!")

    def test_calcular_flete(self):
        self.assertEqual(self._boa1.impuestos, 20.2)

    def test_alimentar_boa(self):
        self._boa1.comer_raton();
        self.assertEqual(self._boa1.ratones_comidos, 1)

if __name__ == '__main__':
    unittest.main()