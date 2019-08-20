import unittest


def triple_step(n):
    counts = [1, 1, 2]
    if n < 3:
        return counts[n]
    i = 2
    while i < n:
        i += 1
        counts[i % 3] = sum(counts)
    return counts[i % 3]

print(triple_step(100))


class Test(unittest.TestCase):
    def test_triple_step(self):
        self.assertEqual(triple_step(3), 4)
        self.assertEqual(triple_step(7), 44)

if __name__ == "__main__":
    unittest.main()
