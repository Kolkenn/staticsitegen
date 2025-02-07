import unittest
from textnode import *
from htmlnode import *

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_neq(self):
        # Different Text
        node = TextNode("I'm node one", TextType.BOLD)
        node2 = TextNode("I'm node two", TextType.BOLD)
        self.assertNotEqual(node, node2)
        # Different TextType
        node = TextNode("I'm node one", TextType.BOLD)
        node2 = TextNode("I'm node one", TextType.ITALIC)
        self.assertNotEqual(node, node2)
        # Bold vs Link
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.LINK,"www.google.com")
        self.assertNotEqual(node, node2)
    
    def test_repr(self):
        node = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual("TextNode(This is a text node, TextType.BOLD, None)",repr(node))

    def test_text_node_to_html(self):
        node = TextNode("I'm just text!", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag,None)
        self.assertEqual(html_node.value,"I'm just text!")

        node = TextNode("I'm bold!", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag,'b')
        self.assertEqual(html_node.value,"I'm bold!")

        node = TextNode("I'm italic!", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag,'i')
        self.assertEqual(html_node.value,"I'm italic!")

        node = TextNode("I'm code!", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag,'code')
        self.assertEqual(html_node.value,"I'm code!")

        node = TextNode("I'm a link to Google!", TextType.LINK,"www.google.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag,'a')
        self.assertEqual(html_node.value,"I'm a link to Google!")
        self.assertEqual(html_node.props,{'href':'www.google.com'})

        node = TextNode("Image of cute cats!", TextType.IMAGE,"www.catsarecute.org/photo_of_fluffy.png")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag,'img')
        self.assertEqual(html_node.value,"")
        self.assertEqual(html_node.props,{'src':'www.catsarecute.org/photo_of_fluffy.png','alt':'Image of cute cats!'})
        
        node = TextNode("This will raise an exception.",'Exception')
        with self.assertRaises(ValueError):
            text_node_to_html_node(node)
    


if __name__ == "__main__":
    unittest.main()