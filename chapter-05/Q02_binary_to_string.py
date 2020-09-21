import unittest


def binary_to_string(n):
    if n >= 1 or n < 0:
        raise Exception("Out of bounds")

    binary = "0."
    while n > 0:
        if len(binary) >= 32:
            raise Exception("Insufficient precision")

        r = n * 2
        if r >= 1:
            binary += "1"
            n = r - 1
        else:
            binary += "0"
            n = r
    return binary


class Test(unittest.TestCase):
    def test_binary_to_string(self):
        self.assertEqual("0.11", binary_to_string(0.75))
        self.assertEqual("0.101", binary_to_string(0.625))
        with self.assertRaises(Exception) as context:
            res = binary_to_string(0.123837)
        self.assertTrue("Insufficient precision" in str(context.exception))
        with self.assertRaises(Exception) as context:
            res = binary_to_string(1.23837)
        self.assertTrue("Out of bounds" in str(context.exception))

