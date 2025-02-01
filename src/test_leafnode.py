import unittest
from htmlnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_repr(self):
        node1 = LeafNode("p", "This is a paragraph of text.")
        self.assertEqual(repr(node1),"LeafNode(p, This is a paragraph of text., None)")

        node2 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(repr(node2),"LeafNode(a, Click me!, {'href': 'https://www.google.com'})")

    def test_tohtml(self):
        # no value test - raise a ValueError
        node = LeafNode("a",None)
        self.assertRaises(ValueError,node.to_html)
        
        # no tag test - return value as raw text.
        node = LeafNode(None,"Click me!",'{"href": "https://www.google.com"}')
        self.assertEqual(node.to_html(),"Click me!")

        # general output tests - verifing the method output.
        node = LeafNode("p", "This is a paragraph of text.")
        self.assertEqual(node.to_html(),'<p>This is a paragraph of text.</p>')
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(),'<a href="https://www.google.com">Click me!</a>')

        


if __name__ == "__main__":
    unittest.main()