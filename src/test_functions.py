import unittest
from textnode import *
from functions import split_nodes_delimiter

class TestTextNode(unittest.TestCase):
    def test_node_delimited(self):
        node = [TextNode("This is text with a `code block` word", TextType.TEXT),TextNode("This is text with a **bolded phrase** in the middle", TextType.TEXT)]
        valid_delims = {'`':TextType.CODE,
                        '**':TextType.BOLD,
                        '*':TextType.ITALIC}    
        
        new_nodes = split_nodes_delimiter(split_nodes_delimiter(split_nodes_delimiter(node,"`",TextType.CODE),"**",TextType.BOLD),"*",TextType.ITALIC)
        self.assertIsInstance(new_nodes,list)
        self.assertEqual(new_nodes[1].text_type,TextType.CODE)
        self.assertEqual(new_nodes[4].text_type,TextType.BOLD)

    def test_delimited_exceptions(self):
        node = [TextNode("This text has an *error in the syntax.",TextType.TEXT)]
        with self.assertRaises(ValueError):
            new_nodes = split_nodes_delimiter(split_nodes_delimiter(split_nodes_delimiter(node,"`",TextType.CODE),"**",TextType.BOLD),"*",TextType.ITALIC)


if __name__ == "__main__":
    unittest.main()