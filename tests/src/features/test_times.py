import unittest 
from features.times import times

class TestSubFunction(unittest.TestCase):
    def test_times_two_elements(self):
        self.assertEqual(times(3, 2), 6)

if __name__ == '__main__':
    unittest.main()