import unittest
from Q3_set_of_stacks import SetOfStacks


class SetOfStacksTest(unittest.TestCase):
    def test_set_of_stacks(self):
        stack = SetOfStacks(2)
        self.assertRaises(ValueError, stack.pop)
        stack.push(1)
        stack.push(2)
        self.assertEqual(2, stack.pop())
        stack.push(3)
        stack.push(4)
        self.assertEqual(4, stack.pop())
        stack.pop()
        self.assertEqual(1, stack.pop())
        self.assertRaises(ValueError, stack.pop)
