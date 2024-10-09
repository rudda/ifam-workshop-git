# tests/src/features/test_add.py
import unittest
from src.features.add import add

class TestAdd(unittest.TestCase):
    def test_add_positive_numbers(self):
        self.assertEqual(add(2, 3), 5)

    def test_add_negative_numbers(self):
        self.assertEqual(add(-1, -1), -2)

    def test_add_zero(self):
        self.assertEqual(add(0, 5), 5)

    def test_wrong_param(self):
        self.assertEqual(add(0, 'a'), None)    

if __name__ == '__main__':
    unittest.main()
