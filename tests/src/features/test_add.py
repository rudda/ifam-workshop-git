import unittest
from features.add import *

class TestAddFunction(unittest.TestCase):
    
    # Testa a soma de dois elementos
    def test_add_two_elements(self):
        self.assertEqual(add(1, 2), 3)
    
    # # Testa a soma de três elementos
    def test_add_three_elements(self):
        self.assertEqual(add_three(1, 2, 3), 6)
        self.assertEqual(add_three(10, -5, 2), 7)
        self.assertAlmostEqual(add_three(1.5, 2.5, 3), 7.0)
    
    # Testa a soma de quatro ou mais elementos
    def test_add_multiple_elements(self):
        self.assertEqual(add_multiple_elements(1, 2, 3, 4), 10)
        self.assertEqual(add_multiple_elements(10, 20, 30, 40, 50), 150)
        self.assertAlmostEqual(add_multiple_elements(1.1, 2.2, 3.3, 4.4), 11.0)

    # # Testa parâmetros inválidos
    def test_invalid_params(self):
        self.assertEqual(add_invalid_params(1, 'a', 3), None)  # Um dos parâmetros é inválido
        self.assertEqual(add_invalid_params('b', 2, 3), None)  # Um dos parâmetros é inválido
        self.assertEqual(add_invalid_params('a', 'b', 'c'), None)  # Todos os parâmetros são inválidos
        self.assertEqual(add_invalid_params(1, 2, 3), "OK")
    
    # # Testa soma com apenas um elemento
    def test_single_element(self):
        self.assertEqual(add_one_element(5), 5)
        self.assertEqual(add_one_element(0), 0)

    # # Testa soma sem parâmetros (deve retornar 0, pois a soma de nada é zero)
    def test_no_elements(self):
        self.assertEqual(add_no_elements(), 0)

if __name__ == '__main__':
    unittest.main()
