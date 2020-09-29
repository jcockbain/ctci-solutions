import unittest


def xml_encoding(xml_object, mapping):
    res = [str(mapping[xml_object.element])]
    for tag, val in xml_object.attributes.items():
        res.append(str(mapping[tag]))
        res.append(str(val))
    res.append("0")

    if xml_object.value:
        res.append(xml_object.value)
        res.append("0")
    else:
        for child in xml_object.children:
            res.append(xml_encoding(child, mapping))
            res.append("0")

    return " ".join(res)


class XMLObject:
    def __init__(self, element, attributes=None, children=None, value=None):
        self.element = element
        self.value = value
        self.attributes = attributes if attributes else {}
        self.children = children if children else []


class Test(unittest.TestCase):
    def test_xml_encoding(self):
        mapping = {"family": 1, "person": 2, "firstName": 3, "lastName": 4, "state": 5}
        xml_object = XMLObject(
            "family",
            {"lastName": "McDowell", "state": "CA"},
            [XMLObject("person", {"firstName": "Gayle"}, [], "Some Message")],
        )
        expected = "1 4 McDowell 5 CA 0 2 3 Gayle 0 Some Message 0 0"
        self.assertEqual(expected, xml_encoding(xml_object, mapping))
