import unittest
from factorial import factorial

class TestFactorial(unittest.TestCase):
    def test_factorial_logic(self):
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(0), 1)

if __name__ == '__main__':
    unittest.main()
