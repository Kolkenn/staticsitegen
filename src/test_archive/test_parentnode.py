import unittest

from htmlnode import *

class TestParentNode(unittest.TestCase):
    def test_repr(self):
        node = ParentNode("p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(repr(node),"ParentNode(p, children: [LeafNode(b, Bold text, None), LeafNode(None, Normal text, None), LeafNode(i, italic text, None), LeafNode(None, Normal text, None)], None)")

    def test_toHTML(self):
        # Test Case from Boot.dev
        node = ParentNode("p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(node.to_html(),"<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")

        # Nested Parents
        node = ParentNode("p",
            [
                LeafNode("b", "Bold text"),
                ParentNode("p",[
                    LeafNode("b","Bold Text 2"),
                    LeafNode(None,"Normal text 2")
                ]),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(node.to_html(),"<p><b>Bold text</b><p><b>Bold Text 2</b>Normal text 2</p>Normal text<i>italic text</i>Normal text</p>")

        # No Children
        node = ParentNode("p",[])
        self.assertEqual(node.to_html(),"<p></p>")
    
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
        


if __name__ == "__main__":
    unittest.main()