import unittest
from src.math_utils import sumar, multiplicar

class TestMathUtils(unittest.TestCase):
    
    def test_sumar(self):
        self.assertEqual(sumar(2, 3), 5)
        self.assertEqual(sumar(-1, 1), 0)

    def test_multiplicar(self):
        self.assertEqual(multiplicar(3, 4), 12)
        self.assertEqual(multiplicar(0, 5), 0)

if __name__ == '__main__':
    unittest.main()