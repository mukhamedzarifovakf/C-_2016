__author__ = 'student'
import unittest
import math
import lib
class LibTest(unittest.TestCase):
    def test_even(self):
        self.assertEqual(lib.even(0), True)
        self.assertEqual(lib.even(1), False)
        self.assertEqual(lib.even(-1), False)
        self.assertEqual(lib.even(2), True)
    def test_factorial(self):
        self.assertEqual(lib.factorial(1), 1)
        self.assertEqual(lib.factorial(3), 6)
        self.assertEqual(lib.factorial(0), 1)
        self.assertEqual(lib.factorial(-1), 1)
    def test_palindrome(self):
        self.assertEqual(lib.palindrome('a'), True)
        self.assertEqual(lib.palindrome('ahh'), False)
        self.assertEqual(lib.palindrome('aha'), True)
    def test_prime(self):
        self.assertEqual(lib.prime(2), True)
        self.assertEqual(lib.prime(4), False)
        self.assertEqual(lib.prime(1), False)
    def test_sin(self):
        self.assertEqual(lib.sin(math.pi), 0)
        self.assertEqual(lib.sin(0), 0)
        self.assertEqual(lib.sin(-(math.pi)/2), -1)
    
unittest.main(verbosity=2)