import unittest


def urlify(string, length):
    new_index = len(string)
    res = [s for s in string]
    for i in reversed(range(length)):
        if res[i] == " ":
            res[new_index - 3 : new_index] = "%20"
            new_index -= 3
        else:
            res[new_index - 1] = string[i]
            new_index -= 1

    return "".join(res)


class Test(unittest.TestCase):
    def test_urlify(self):
        self.assertEqual("Mr%20John%20Smith", urlify("Mr John Smith    ", 13))


if __name__ == "__main__":
    unittest.main()
