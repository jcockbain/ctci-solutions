import unittest


def is_palindrome_permutation(phrase):
    table = [0 for _ in range(ord("z") - ord("a") + 1)]
    countodd = 0
    for c in phrase:
        x = char_number(c)
        if x != -1:
            table[x] += 1
            if table[x] % 2:
                countodd += 1
            else:
                countodd -= 1
    return countodd <= 1


def char_number(c):
    a = ord("a")
    z = ord("z")
    A = ord("A")
    Z = ord("Z")
    val = ord(c)

    if a <= val <= z:
        return val - a
    elif A <= val <= Z:
        return val - A
    return -1


class palindrome_permutation_test(unittest.TestCase):
    def test_palindrome_permutation(self):
        self.assertEqual(True, is_palindrome_permutation("acbbac"))
        self.assertEqual(False, is_palindrome_permutation("asdasdsa"))


if __name__ == "__main__":
    unittest.main()
