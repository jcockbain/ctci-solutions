import unittest


def get_bit(n, j):
    return (n & (1 << j)) != 0


def missing_number(nums, n):
    mask, bit, j = 1, 0, 0
    while mask <= n:
        count_0, count_1 = 0, 0
        for i in nums:
            if get_bit(i, j):
                count_1 += 1
            else:
                count_0 += 1
        if count_1 >= count_0:
            nums = [x for x in nums if not (x & mask)]
        else:
            bit |= mask
            nums = [x for x in nums if (x & mask)]
        mask <<= 1
        j += 1
    return bit


class Test(unittest.TestCase):
    def test_get_bit(self):
        self.assertEqual(True, get_bit(1, 0))
        self.assertEqual(False, get_bit(2, 0))
        self.assertEqual(True, get_bit(2, 1))
        self.assertEqual(True, get_bit(8, 3))

    def test_missing_number(self):
        self.assertEqual(8, missing_number([0, 1, 2, 3, 4, 5, 6, 7, 9], 9))
        self.assertEqual(3, missing_number([0, 1, 2, 4, 5, 6, 7, 8, 9], 9))
        self.assertEqual(5, missing_number([0, 1, 4, 3, 2, 6], 6))
        nums = [x for x in range(101)]
        nums.remove(56)
        self.assertEqual(56, missing_number(nums, 100))
