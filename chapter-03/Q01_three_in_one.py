import unittest


class MultiStack:
    def __init__(self, stacksize):
        self.numstacks = 3
        self.array = [0] * (stacksize * self.numstacks)
        self.sizes = [0] * self.numstacks
        self.stacksize = stacksize

    def push(self, item, stacknum):
        if self.isFull(stacknum):
            raise Exception("Stack is full")
        self.sizes[stacknum] += 1
        self.array[self.indexOfTop(stacknum)] = item

    def pop(self, stacknum):
        if self.isEmpty(stacknum):
            raise Exception("Stack is empty")
        value = self.array[self.indexOfTop(stacknum)]
        self.array[self.indexOfTop(stacknum)] = 0
        self.sizes[stacknum] -= 1
        return value

    def peek(self, stacknum):
        if self.isEmpty(stacknum):
            raise Exception("Stack is empty")
        return self.array[self.indexOfTop(stacknum)]

    def isEmpty(self, stacknum):
        return self.sizes[stacknum] == 0

    def isFull(self, stacknum):
        return self.sizes[stacknum] == self.stacksize

    def indexOfTop(self, stacknum):
        offset = stacknum * self.stacksize
        return offset + self.sizes[stacknum] - 1


class Test(unittest.TestCase):
    def test_multistack(self):
        newstack = MultiStack(4)
        with self.assertRaises(Exception) as context:
            newstack.pop(1)
        self.assertTrue("Stack is empty" in str(context.exception))
        self.assertEqual(True, newstack.isEmpty(1))
        newstack.push(3, 1)
        newstack.push(2, 2)
        self.assertEqual(3, newstack.peek(1))
        self.assertEqual(2, newstack.pop(2))
        self.assertEqual(3, newstack.peek(1))
        self.assertEqual(False, newstack.isEmpty(1))
        newstack.push(2, 1)
        newstack.push(3, 1)
        newstack.push(4, 1)
        with self.assertRaises(Exception) as context:
            newstack.push(5, 1)
        self.assertTrue("Stack is full" in str(context.exception))
        self.assertEqual(4, newstack.pop(1))
        self.assertEqual(3, newstack.pop(1))
        self.assertEqual(2, newstack.pop(1))
        self.assertEqual(3, newstack.pop(1))
        with self.assertRaises(Exception) as context:
            newstack.peek(1)
        self.assertTrue("Stack is empty" in str(context.exception))
