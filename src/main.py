from textnode import TextNode,TextType
from htmlnode import ParentNode,LeafNode
from block_functions import markdown_to_blocks

def main():    
    markdown = "# This is a heading\n\n     This is a paragraph of text. It has some **bold** and *italic* words inside of it.\n\n* This is the first list item in a list block\n* This is a list item\n* This is another list item"
    print(markdown_to_blocks(markdown))

main()