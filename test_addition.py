import unittest
from addition_function import add

class Testadd(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(5), 10)
        self.assertEqual(add(-5), "Number is Negative" -10)

if __name__ == "__main__":
    unittest.main()