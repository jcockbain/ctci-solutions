import unittest


class DLinkedNode:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity):
        self.cache = {}
        self.size = 0
        self.capacity = capacity
        self.head = DLinkedNode()
        self.tail = DLinkedNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _add_node(self, node):
        node.prev = self.head
        node.next = self.head.next

        self.head.next.prev = node
        self.head.next = node

    def _remove_node(self, node):
        prev = node.prev
        new = node.next

        prev.next = new
        new.prev = prev

    def _move_to_head(self, node):
        self._remove_node(node)
        self._add_node(node)

    def _pop_tail(self):
        res = self.tail.prev
        self._remove_node(res)
        return res

    def get(self, key):
        node = self.cache.get(key, None)
        if not node:
            return None
        self._move_to_head(node)
        return node.value

    def add(self, key, value):
        node = self.cache.get(key)
        if not node:
            new_node = DLinkedNode(key, value)
            self.cache[key] = new_node
            self._add_node(new_node)
            self.size += 1

            if self.size > self.capacity:
                tail = self._pop_tail()
                del self.cache[tail.key]
                self.size -= 1

        else:
            node.value = value
            self._move_to_head(node)


class Test(unittest.TestCase):
    def test_pairs_with_sum(self):
        lru_cache = LRUCache(3)
        lru_cache.add(1, 2)
        lru_cache.add(2, 5)
        lru_cache.add(3, 4)

        self.assertEqual(5, lru_cache.get(2))
        self.assertEqual(2, lru_cache.get(1))
        self.assertEqual(4, lru_cache.get(3))

        # removes key 2 from cache

        lru_cache.add(4, 10)
        self.assertEqual(None, lru_cache.get(2))

        # changes value for key 1

        lru_cache.add(1, 7)
        self.assertEqual(7, lru_cache.get(1))
