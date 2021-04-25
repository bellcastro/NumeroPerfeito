import unittest

from numeroPerfeito import numeroPerfeito


class TestMethod(unittest.TestCase):
    def test_case1(self):
        self.assertEqual(numeroPerfeito(6), True, "O Número 6 é perfeito.")

    def test_case2(self):
        self.assertEqual(numeroPerfeito(10), False, "O Número 10 não é perfeito.")

if __name__ == '__main__':
  unittest.main()
