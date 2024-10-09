import unittest

class TestSubFunction(unittest.TestCase):
    
    # Testa a subtração com números inteiros
    def test_sub_integers(self):
        self.assertEqual(sub(10, 2), 8)
        self.assertEqual(sub(10, -2), 12)
        self.assertEqual(sub(-10, 2), -12)
        self.assertEqual(sub(-10, -2), -8)

    # Testa a subtração com números float
    def test_sub_floats(self):
        self.assertAlmostEqual(sub(7.5, 2.5), 5.0)
        self.assertAlmostEqual(sub(2.5, 7.5), -5.0)
        self.assertAlmostEqual(sub(-7.5, 2.5), -10.0)
    
    # Testa parâmetros inválidos
    def test_invalid_params(self):
        self.assertEqual(sub(10, 'a'), None)  # Subtraendo inválido
        self.assertEqual(sub('b', 2), None)   # Minuendo inválido
        self.assertEqual(sub('a', 'b'), None) # Ambos inválidos

    # Testa a subtração envolvendo zero
    def test_sub_with_zero(self):
        self.assertEqual(sub(0, 10), -10)
        self.assertEqual(sub(10, 0), 10)
        self.assertEqual(sub(0, 0), 0)

if __name__ == '__main__':
    unittest.main()
