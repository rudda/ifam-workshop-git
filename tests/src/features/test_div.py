import unittest
from features.div import div

class TestDivFunction(unittest.TestCase):
    
    # Testa a divisão correta com números inteiros
    def test_div_integers(self):
        self.assertEqual(div(10, 2), 5)
        self.assertEqual(div(-10, 2), -5)
        self.assertEqual(div(10, -2), -5)
    
    # Testa a divisão correta com números float
    def test_div_floats(self):
        self.assertAlmostEqual(div(7.5, 2.5), 3.0)
        self.assertAlmostEqual(div(-7.5, 2.5), -3.0)
    
    # Testa divisão por zero
    def test_div_by_zero(self):
        self.assertEqual(div(10, 0), None)
        self.assertEqual(div(0, 0), None)
    
    # Testa parâmetros inválidos
    def test_invalid_params(self):
        self.assertEqual(div(10, 'a'), None)  # Dividendo inválido
        self.assertEqual(div('b', 2), None)   # Divisor inválido
        self.assertEqual(div('a', 'b'), None) # Ambos inválidos

    # Testa divisão com zero como numerador
    def test_div_numerator_zero(self):
        self.assertEqual(div(0, 10), 0)
        self.assertEqual(div(0, 2.5), 0)

if __name__ == '__main__':
    unittest.main()
