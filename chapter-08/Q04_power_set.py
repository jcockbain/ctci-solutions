import unittest


def find_subsets(master_set, index=0):
    def backtrack(start, end, temp):
        output.append(temp[:])
        for i in range(start, end):
            temp.append(master_set[i])
            backtrack(i + 1, end, temp)
            temp.pop()

    output = []
    backtrack(0, len(master_set), [])
    return output


class test(unittest.TestCase):
    def test_find_subsets(self):
        test_set = [1, 2, 3]
        expected = [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]
        self.assertListEqual(sorted(find_subsets(test_set)), sorted(expected))


if __name__ == "__main__":
    unittest.main()
