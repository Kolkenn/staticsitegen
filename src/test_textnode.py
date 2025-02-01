import unittest
from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_neq_text(self):
        node = TextNode("I'm node one", TextType.BOLD)
        node2 = TextNode("I'm node two", TextType.BOLD)
        self.assertNotEqual(node, node2)
    
    def test_neq_url(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD,"www.google.com")
        self.assertNotEqual(node, node2)

    def test_neq_text_type(self):
        node = TextNode("This is a text node", TextType.ITALIC)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)
    
    def test_repr(self):
        node = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual("TextNode(This is a text node, bold, None)",repr(node))
    
    


if __name__ == "__main__":
    unittest.main()