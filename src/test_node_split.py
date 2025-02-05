import unittest
from textnode import *
from functions import *

class TestNodeSplit(unittest.TestCase):
    def test_split_nodes_image(self):
        node = TextNode("![Beginning Link](https://willthiswork.com) will it work, I wonder? ![For Help Click Here](https://needhelpcoding.com)",TextType.TEXT)
        self.assertListEqual(split_nodes_image([node]),[TextNode("Beginning Link", TextType.IMAGE, "https://willthiswork.com"), 
                                                        TextNode(" will it work, I wonder? ", TextType.TEXT, None), 
                                                        TextNode("For Help Click Here", TextType.IMAGE, "https://needhelpcoding.com")])
        
        node = TextNode("This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)",TextType.TEXT)
        self.assertListEqual(split_nodes_image([node]),[TextNode("This is text with a ", TextType.TEXT, None), 
                                                        TextNode("rick roll", TextType.IMAGE, "https://i.imgur.com/aKaOqIh.gif"), 
                                                        TextNode(" and ", TextType.TEXT, None), 
                                                        TextNode("obi wan", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg")])
        
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            ],
            new_nodes,
        )

    def test_split_nodes_link(self):
        node = TextNode("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",TextType.TEXT,)
        self.assertEqual(split_nodes_link([node]),[TextNode("This is text with a link ", TextType.TEXT, None), 
                                                   TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"), 
                                                   TextNode(" and ", TextType.TEXT, None), 
                                                   TextNode("to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev")])   

    def test_split_image_single(self):
        node = TextNode(
            "![image](https://www.example.COM/IMAGE.PNG)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("image", TextType.IMAGE, "https://www.example.COM/IMAGE.PNG"),
            ],
            new_nodes,
        )

    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_split_links(self):
        node = TextNode(
            "This is text with a [link](https://boot.dev) and [another link](https://blog.boot.dev) with text that follows",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://boot.dev"),
                TextNode(" and ", TextType.TEXT),
                TextNode("another link", TextType.LINK, "https://blog.boot.dev"),
                TextNode(" with text that follows", TextType.TEXT),
            ],
            new_nodes,
        )

if __name__ == "__main__":
    unittest.main()