import unittest


def string_compression(s):
    if len(s) == 0:
        return s

    res = []
    current_letter, current_count = s[1], 1
    for c in s[1:]:
        if c == current_letter:
            current_count += 1
        else:
            res.append(current_letter)
            res.append(str(current_count))
            current_letter = c
            current_count = 1
    final_compressed = "".join(res + [current_letter, str(current_count)])
    return final_compressed if len(final_compressed) < len(s) else s


class Test(unittest.TestCase):
    def test_string_compression(self):
        self.assertEqual("a2b1c5a3", string_compression("aabcccccaaa"))
        self.assertEqual("a6", string_compression("aaaaaa"))
        self.assertEqual("a6A2B3", string_compression("aaaaaaAABBB"))

        self.assertEqual("abc", string_compression("abc"))
        self.assertEqual("aBCD", string_compression("aBCD"))
