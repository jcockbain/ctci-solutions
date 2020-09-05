import unittest
from Q01_route_between_nodes import route_between_nodes


class RouteBetweenNodesTest(unittest.TestCase):
    def test_route_between_nodes(self):
        test_graph = {"a": ["b"], "b": ["c"], "c": []}
        result = route_between_nodes(test_graph, "a", "c")
        self.assertEqual(["a", "b", "c"], result)

    def test_route_between_nodes(self):
        test_graph = {"a": ["c"], "b": [""], "c": ["b"]}
        result = route_between_nodes(test_graph, "a", "b")
        self.assertEqual(["a", "c", "b"], result)


if __name__ == "__main__":
    unittest.main()
