import unittest


class Name:
    def __init__(self, name, count=0):
        self.name = name
        self.synonyms = []
        self.count = count


def baby_names(names, synonyms):
    graph = {}
    for person in names:
        name, count = person
        graph[name] = Name(name, count)

    for synonym in synonyms:
        name_1, name_2 = synonym

        if name_1 not in graph:
            graph[name_1] = Name(name_1)
        if name_2 not in graph:
            graph[name_2] = Name(name_2)

        graph[name_1].synonyms.append(graph[name_2])
        graph[name_2].synonyms.append(graph[name_1])

    visited = set()
    result = {}

    def dfs(root):
        if root in visited:
            return 0
        visited.add(root)
        res = root.count
        for node in root.synonyms:
            res += dfs(node)
        return res

    for person in graph:
        root = graph[person]
        if root not in visited:
            result[person] = dfs(root)

    return [(name, result[name]) for name in result]


class Test(unittest.TestCase):
    def test_baby_names(self):
        names = [
            ("John", 15),
            ("Jon", 12),
            ("Chris", 13),
            ("Kris", 4),
            ("Christopher", 19),
        ]
        synonyms = [
            ("Jon", "John"),
            ("John", "Johnny"),
            ("Chris", "Kris"),
            ("Chris", "Christopher"),
            ("Christian", "Christopher"),
        ]
        self.assertEqual([("John", 27), ("Chris", 36)], baby_names(names, synonyms))

