import unittest


def sparse_similarity(documents):
    intersections = {}
    ids = list(documents.keys())
    for i in range(len(ids)):
        id_1 = ids[i]
        for j in range(i + 1, len(ids)):
            id_2 = ids[j]
            arr_1, arr_2 = documents[id_1], documents[id_2]
            intersection = get_intersection(arr_1, arr_2)
            if intersection:
                intersections[(id_1, id_2)] = intersection / (
                    len(arr_1) + len(arr_2) - intersection
                )
    return intersections


def get_intersection(a, b):
    return len(set(a) & set(b))


class Test(unittest.TestCase):
    def test_sparse_similarity(self):
        documents = {
            13: [14, 15, 100, 9, 3],
            16: [32, 1, 9, 5, 3],
            19: [15, 29, 2, 6, 8, 7],
            24: [7, 10],
        }
        expected = {(13, 19): 0.1, (13, 16): 0.25, (19, 24): 1 / 7}
        self.assertEqual(expected, sparse_similarity(documents))
