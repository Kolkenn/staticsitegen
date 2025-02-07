import unittest
from textnode import *
from inline_functions import split_nodes_delimiter

class TestDelimiter(unittest.TestCase):
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
    
    def test_delim_bold(self):
        node = TextNode("This is text with a **bolded** word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bolded", TextType.BOLD),
                TextNode(" word", TextType.TEXT),
            ],
            new_nodes
        )

    def test_delim_bold_double(self):
        node = TextNode(
            "This is text with a **bolded** word and **another**", TextType.TEXT
        )
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bolded", TextType.BOLD),
                TextNode(" word and ", TextType.TEXT),
                TextNode("another", TextType.BOLD),
            ],
            new_nodes,
        )

    def test_delim_bold_multiword(self):
        node = TextNode(
            "This is text with a **bolded word** and **another**", TextType.TEXT
        )
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bolded word", TextType.BOLD),
                TextNode(" and ", TextType.TEXT),
                TextNode("another", TextType.BOLD),
            ],
            new_nodes,
        )

    def test_delim_italic(self):
        node = TextNode("This is text with an *italic* word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "*", TextType.ITALIC)
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_delim_bold_and_italic(self):
        node = TextNode("**bold** and *italic*", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        new_nodes = split_nodes_delimiter(new_nodes, "*", TextType.ITALIC)
        self.assertListEqual(
            [
                TextNode("bold", TextType.BOLD),
                TextNode(" and ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
            ],
            new_nodes,
        )

    def test_delim_code(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" word", TextType.TEXT),
            ],
            new_nodes,
        )
        


if __name__ == "__main__":
    unittest.main()