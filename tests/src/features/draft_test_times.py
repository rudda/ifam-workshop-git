import unittest
from features.times import times

class TestTimesFunction(unittest.TestCase):
    
    # Testa a multiplicação com números inteiros
    def test_times_integers(self):
        self.assertEqual(times(10, 2), 20)
        self.assertEqual(times(10, -2), -20)
        self.assertEqual(times(-10, 2), -20)
        self.assertEqual(times(-10, -2), 20)

    # Testa a multiplicação com números float
    def test_times_floats(self):
        self.assertAlmostEqual(times(7.5, 2.5), 18.75)
        self.assertAlmostEqual(times(2.5, -7.5), -18.75)
        self.assertAlmostEqual(times(-7.5, 2.5), -18.75)
    
    # Testa a multiplicação por zero
    def test_times_with_zero(self):
        self.assertEqual(times(0, 10), 0)
        self.assertEqual(times(10, 0), 0)
        self.assertEqual(times(0, 0), 0)

    # Testa parâmetros inválidos
    def test_invalid_params(self):
        self.assertEqual(times(10, 'a'), None)  # Multiplicador inválido
        self.assertEqual(times('b', 2), None)   # Multiplicando inválido
        self.assertEqual(times('a', 'b'), None) # Ambos inválidos

if __name__ == '__main__':
    unittest.main()
