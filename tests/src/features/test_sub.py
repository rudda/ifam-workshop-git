import unittest 
from features.sub import sub

class TestSubFunction(unittest.TestCase):
    def test_sub_two_elements(self):
        self.assertEqual(sub(3, 2), 1)

if __name__ == '__main__':
    unittest.main()