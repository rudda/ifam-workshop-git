import unittest

class TestAddFunction(unittest.TestCase):
    
    # Testa a soma de dois elementos
    def test_add_two_elements(self):
        self.assertEqual(add(1, 2), 3)
    
    # Testa a soma de três elementos
    def test_add_three_elements(self):
        self.assertEqual(add(1, 2, 3), 6)
        self.assertEqual(add(10, -5, 2), 7)
        self.assertAlmostEqual(add(1.5, 2.5, 3), 7.0)
    
    # Testa a soma de quatro ou mais elementos
    def test_add_multiple_elements(self):
        self.assertEqual(add(1, 2, 3, 4), 10)
        self.assertEqual(add(10, 20, 30, 40, 50), 150)
        self.assertAlmostEqual(add(1.1, 2.2, 3.3, 4.4), 11.0)

    # Testa parâmetros inválidos
    def test_invalid_params(self):
        self.assertEqual(add(1, 'a', 3), None)  # Um dos parâmetros é inválido
        self.assertEqual(add('b', 2, 3), None)  # Um dos parâmetros é inválido
        self.assertEqual(add('a', 'b', 'c'), None)  # Todos os parâmetros são inválidos
    
    # Testa soma com apenas um elemento
    def test_single_element(self):
        self.assertEqual(add(5), 5)
        self.assertEqual(add(0), 0)

    # Testa soma sem parâmetros (deve retornar 0, pois a soma de nada é zero)
    def test_no_elements(self):
        self.assertEqual(add(), 0)

if __name__ == '__main__':
    unittest.main()
