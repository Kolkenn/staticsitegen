import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_repr(self):
        test_prop = {"href": "https://www.google.com",
                     "target": "_blank",}
        node = HTMLNode(tag="h1",value="Header",props=test_prop)
        self.assertEqual(repr(node),"HTMLNode(h1, Header, None, {'href': 'https://www.google.com', 'target': '_blank'})")

    def test_props_to_html(self):
        test_prop = {"href": "https://www.google.com",
                     "target": "_blank",}
        node = HTMLNode(props=test_prop)
        self.assertEqual(node.props_to_html(),' href="https://www.google.com" target="_blank"')

    def test_blank(self):
        node = HTMLNode()
        self.assertEqual(node.__repr__(),"HTMLNode(None, None, None, None)")

    def test_toHTML(self):
        node = HTMLNode()
        node.to_html
        self.assertRaises(NotImplementedError)

    def test_values(self):
        node = HTMLNode(
            "div",
            "I wish I could read",
        )
        self.assertEqual(
            node.tag,
            "div",
        )
        self.assertEqual(
            node.value,
            "I wish I could read",
        )
        self.assertEqual(
            node.children,
            None,
        )
        self.assertEqual(
            node.props,
            None,
        )


if __name__ == "__main__":
    unittest.main()