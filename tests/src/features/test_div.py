import unittest
from features.div import *

class TestDivFunction(unittest.TestCase):
    
    # Testa a divisão correta com números inteiros
    def test_div_integers(self):
        self.assertEqual(div_integers(10, 2), 5)
        self.assertEqual(div_integers(-10, 2), -5)
        self.assertEqual(div_integers(10, -2), -5)
    
    # Testa a divisão correta com números float
    def test_div_floats(self):
        self.assertAlmostEqual(div_floats(7.5, 2.5), 3.0)
        self.assertAlmostEqual(div_floats(-7.5, 2.5), -3.0)
    
    # Testa divisão por zero
    def test_div_by_zero(self):
        self.assertEqual(div_by_zero(10, 0), None)
        self.assertEqual(div_by_zero(0, 0), None)
    
    # Testa parâmetros inválidos
    def test_invalid_params(self):
        self.assertEqual(div_invalid_params(10, 'a'), None)  # Dividendo inválido
        self.assertEqual(div_invalid_params('b', 2), None)   # Divisor inválido
        self.assertEqual(div_invalid_params('a', 'b'), None) # Ambos inválidos

    # Testa divisão com zero como numerador
    def test_div_numerator_zero(self):
        self.assertEqual(div_numerator_zero(0, 10), 0)
        self.assertEqual(div_numerator_zero(0, 2.5), 0)

if __name__ == '__main__':
    unittest.main()
