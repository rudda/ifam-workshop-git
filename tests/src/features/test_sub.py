import unittest
from features.sub import *

class TestSubFunction(unittest.TestCase):
    
    # Testa a subtração com números inteiros
    def test_sub_integers(self):
        self.assertEqual(sub_integers(10, -2), 12)
        self.assertEqual(sub_integers(10, 2), 8)
        self.assertEqual(sub_integers(-10, 2), -12)
        self.assertEqual(sub_integers(-10, -2), -8)

    # Testa a subtração com números float
    def test_sub_floats(self):
        self.assertAlmostEqual(sub_floats(7.5, 2.5), 5.0)
        self.assertAlmostEqual(sub_floats(2.5, 7.5), -5.0)
        self.assertAlmostEqual(sub_floats(-7.5, 2.5), -10.0)
    
    # Testa parâmetros inválidos
    def test_invalid_params(self):
        self.assertEqual(sub_invalid_params(10, 'a'), None)  # Subtraendo inválido
        self.assertEqual(sub_invalid_params('b', 2), None)   # Minuendo inválido
        self.assertEqual(sub_invalid_params('a', 'b'), None) # Ambos inválidos
        self.assertEqual(sub_invalid_params(2, 2), "OK")

    # Testa a subtração envolvendo zero
    def test_sub_with_zero(self):
        self.assertEqual(sub_with_zero(0, 10), -10)
        self.assertEqual(sub_with_zero(10, 0), 10)
        self.assertEqual(sub_with_zero(0, 0), 0)
        
     # Testa a subtração com três ou mais inteiros
    def test_sub_multiple_integers(self):
        self.assertEqual(sub_multiple_integers(10, 2, 3), 5)  # 10 - 2 - 3 = 5
        self.assertEqual(sub_multiple_integers(50, 20, 10, 5), 15)  # 50 - 20 - 10 - 5 = 15
        self.assertEqual(sub_multiple_integers(-10, -5, 5), 0)  # -10 - (-5) - 5 = 0

    # Testa a subtração com números float e inteiros misturados
    def test_sub_mixed_types(self):
        self.assertAlmostEqual(sub_mixed_types(10.5, 2.5, 3), 5.0)  # 10.5 - 2.5 - 3 = 5.0
        self.assertAlmostEqual(sub_mixed_types(0, 2, 1.5), -3.5)  # 0 - 2 - 1.5 = -3.5

    # Testa parâmetros inválidos
    # def test_invalid_params(self):
    #     self.assertEqual(sub(10, 5, 'a'), None)  # Um parâmetro inválido
    #     self.assertEqual(sub('b', 2, 1), None)   # Um parâmetro inválido
    #     self.assertEqual(sub('a', 'b', 'c'), None)  # Todos inválidos


if __name__ == '__main__':
    unittest.main()
