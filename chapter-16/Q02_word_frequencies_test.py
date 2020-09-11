import unittest

from Q02_word_frequencies import get_frequency, get_frequency_repeated


class WordFrequenciesTest(unittest.TestCase):
    def test_word_frequencies(self):
        test_string = "hello world, i just wanted to say hello"
        self.assertEqual(2, get_frequency(test_string, "hello"))
        self.assertEqual(2, get_frequency_repeated(test_string, "hello"))
