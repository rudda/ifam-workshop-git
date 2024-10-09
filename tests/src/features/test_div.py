import unittest 
from features.div import div

class TestSubFunction(unittest.TestCase):
    def test_div_two_elements(self):
        self.assertEqual(div(6, 3), 2)

if __name__ == '__main__':
    unittest.main()