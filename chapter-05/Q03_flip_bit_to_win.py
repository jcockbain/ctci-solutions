import unittest


def longest_bit_subsequence_after_flip(n):
    mask = 1 << 31
    longest = 0
    current_with_flip = 0
    current_without_flip = 0

    while mask:
        if mask & n:
            current_without_flip += 1
            current_with_flip += 1
        else:
            current_with_flip = current_without_flip + 1
            current_without_flip = 0
        longest = max(current_with_flip, longest)
        mask >>= 1
    return longest


class Test(unittest.TestCase):
    def test_longest_sunsequence_after_flip(self):
        self.assertEqual(8, longest_bit_subsequence_after_flip(1775))
