import unittest
from collections import deque


def valid_build_order(nodes, dependencies):
    graph = {}
    for node_val in nodes:
        graph[node_val] = Node(node_val)
    for first, second in dependencies:
        graph[first].add_edge(graph[second])
    queue = deque([])
    for node_val in nodes:
        node = graph[node_val]
        if not node.dependencies:
            queue.append(node)
    build_order = []

    while queue:
        node = queue.popleft()
        build_order.append(node.value)
        for dependent in node.edges:
            dependent.dependencies -= 1
            if not dependent.dependencies:
                queue.append(dependent)
    if len(build_order) < len(nodes):
        raise Exception("No valid ordering")
    return build_order


class Node:
    def __init__(self, value):
        self.edges = []
        self.value = value
        self.dependencies = 0

    def add_edge(self, node):
        self.edges.append(node)
        node.dependencies += 1


class Test(unittest.TestCase):
    def test_valid_build_order(self):
        nodes = ["a", "b", "c", "d", "e", "f"]
        dependencies = [("a", "d"), ("f", "b"), ("b", "d"), ("f", "a"), ("d", "c")]
        expected = ["e", "f", "b", "a", "d", "c"]
        self.assertEqual(expected, valid_build_order(nodes, dependencies))

        invalid_dependencies = [("b", "a"), ("a", "c"), ("c", "b")]
        with self.assertRaises(Exception) as context:
            order = valid_build_order(nodes, invalid_dependencies)
        self.assertTrue("No valid ordering" in str(context.exception))
