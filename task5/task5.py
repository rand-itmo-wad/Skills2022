# Author: Rand Deeb
# Version V0.1

import unittest

def factors(n):
    p = 2
    f = list()
    while n >= p*p :
        if n % p == 0:
            f.append(p)
            n = int(n / p)
        else:
           p = p + 1
    f.append(n)
    return f

def is_prime(number):
    if number <= 1:
        return False
    for n in range(2, number):
        if number % n == 0:
            return False
        else:
            return True

def vowels(text):
    v = list()
    for i in text:
        if i in 'aeiouAEIOU':
            v.append(i)
    return v


class TestTask5(unittest.TestCase):
    def test_factors(self):
        self.assertCountEqual(factors(1), [1], "Should be [1]")
        self.assertCountEqual(factors(4), [2, 2], "Should be [2,2]")
        self.assertCountEqual(factors(5), [5], "Should be [5]")
        self.assertCountEqual(factors(6), [2,3], "Should be [2,3]")

    def test_is_prime(self):
        self.assertEqual(is_prime(-1), False, "Should be False")
        self.assertEqual(is_prime(1), False, "Should be False")
        self.assertEqual(is_prime(4), False, "Should be False")
        self.assertEqual(is_prime(5), True, "Should be True")
        self.assertEqual(is_prime(6), False, "Should be False")

    def test_vowels(self):
        self.assertCountEqual(vowels("ok"), ["o"], 'Should be ["o"]')
        self.assertCountEqual(vowels("test"), ["e"], 'Should be ["e"]')
        self.assertCountEqual(vowels("aeiouAEIOU"), ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"], 'Should be ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]')
        self.assertCountEqual(vowels(""), [], "Should be []")

    def test_len(self):
        self.assertEqual(len(""), 0, "Should be 0")
        self.assertEqual(len("test"), 4, "Should be 4")
        self.assertEqual(len("test "), 5, "Should be 5")
        self.assertEqual(len([1, 2]), 2, "Should be 2")

if __name__ == '__main__':
    unittest.main()
