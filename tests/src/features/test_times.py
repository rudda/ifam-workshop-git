import unittest
from features.times import *

class TestTimesFunction(unittest.TestCase):
    
    # Testa a multiplicação com números inteiros
    def test_times_integers(self):
        self.assertEqual(times_integers(10, 2), 20)
        self.assertEqual(times_integers(10, -2), -20)
        self.assertEqual(times_integers(-10, 2), -20)
        self.assertEqual(times_integers(-10, -2), 20)

    # Testa a multiplicação com números float
    def test_times_floats(self):
        self.assertAlmostEqual(times_floats(7.5, 2.5), 18.75)
        self.assertAlmostEqual(times_floats(2.5, -7.5), -18.75)
        self.assertAlmostEqual(times_floats(-7.5, 2.5), -18.75)
    
    # Testa a multiplicação por zero
    def test_times_with_zero(self):
        self.assertEqual(times_with_zero(0, 10), 0)
        self.assertEqual(times_with_zero(10, 0), 0)
        self.assertEqual(times_with_zero(0, 0), 0)

    # Testa parâmetros inválidos
    def test_invalid_params(self):
        self.assertEqual(times_invalid_params(10, 'a'), None)  # Multiplicador inválido
        self.assertEqual(times_invalid_params('b', 2), None)   # Multiplicando inválido
        self.assertEqual(times_invalid_params('a', 'b'), None) # Ambos inválidos
        self.assertEqual(times_invalid_params(2, 2), "OK")

if __name__ == '__main__':
    unittest.main()
