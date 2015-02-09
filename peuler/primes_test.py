__author__ = 'Cam'

import unittest
import primes


class SieveTest(unittest.TestCase):
    def test_one(self):
        with self.assertRaises(ValueError) as _:
            primes.sieve(1)

    def test_two(self):
        self.assertSequenceEqual([2], primes.sieve(2))

    def test_ten(self):
        self.assertSequenceEqual([2, 3, 5, 7], primes.sieve(10))


class FactorizeTest(unittest.TestCase):
    def test_zero(self):
        with self.assertRaises(ValueError) as _:
            primes.factorize(0)

    def test_one(self):
        self.assertEquals([], primes.factorize(1))

    def test_25(self):
        self.assertSequenceEqual([5, 5], primes.factorize(25))

    def test_38(self):
        self.assertSequenceEqual([2, 19], primes.factorize(38))


class NthPrimeTest(unittest.TestCase):
    def test_0(self):
        with self.assertRaises(ValueError) as _:
            primes.nth_prime(0)

    def test_1(self):
        self.assertEquals(2, primes.nth_prime(1))

    def test_to_100(self):
        to_test = [primes.nth_prime(i) for i in xrange(1, 100)]
        correct = primes.sieve(10000)[0:99]
        self.assertSequenceEqual(to_test, correct)


class PrimeApproxTest(unittest.TestCase):
    def test_0(self):
        with self.assertRaises(ValueError) as _:
            primes.approx_nth_prime(0)


class StringRotateTest(unittest.TestCase):
    def test_empty(self):
        rot = primes.string_rotate("")
        self.assertEqual(rot, "")

    def test_once(self):
        rot = primes.string_rotate("4001")
        self.assertEqual(rot, "0014")


class IntRotationsTest(unittest.TestCase):
    def test_1001(self):
        self.assertSequenceEqual(primes.int_rotations(1001), [1001, 11, 110, 1100])


class IsCircularPrimeTest(unittest.TestCase):
    def test_13(self):
        prime_set = primes.sieve(100)
        self.assertTrue(primes.is_circular_prime(prime_set, 13))

    def test_19(self):
        prime_set = primes.sieve(100)
        self.assertFalse(primes.is_circular_prime(prime_set, 19))

if __name__ == '__main__':
    unittest.main()
