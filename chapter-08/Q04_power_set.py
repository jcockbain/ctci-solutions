import unittest


def find_subsets(master_set, index):
    all_subsets = []
    if len(master_set) == index:
        if [] not in all_subsets:
            all_subsets.append([])
    else:
        all_subsets = find_subsets(master_set, index + 1)
        item = master_set[index]
        more_subsets = []
        for subset in all_subsets:
            new_subset = []
            [new_subset.append(value)
                for value in subset if value not in new_subset]
            new_subset.append(item)
            more_subsets.append(new_subset)
            [all_subsets.append(value)
                for value in more_subsets if value not in new_subset]
    return all_subsets


# class test(unittest.TestCase):
#     def test_find_subsets(self):
#         test_set = [1, 2, 3]
#         expected = [[], [1], [2], [3], [12], [123]]
#         self.assertEqual(find_subsets(test_set, 0), expected)


if __name__ == "__main__":
    unittest.main()
