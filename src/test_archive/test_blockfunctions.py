import unittest
from block_functions import *

class TestBlockFunctions(unittest.TestCase):
    def test_ordered_list_block_id(self):
        correct = block_type_olist
        markdown = "1. Carrots\n2. Tomatoes\n3. Onions"
        type = block_to_block_type(markdown)
        self.assertEqual(type,correct)

        correct = block_type_paragraph
        markdown = "1. Carrots\n2. Tomatoes\n3.Onions"
        type = block_to_block_type(markdown)
        self.assertEqual(type,correct)
    
    def test_unordered_list_block_id(self):
        correct = block_type_ulist
        
        markdown = "* Carrots\n* Tomatoes\n* Onions"
        type = block_to_block_type(markdown)
        self.assertEqual(type,correct)

        markdown = "- Carrots\n- Tomatoes\n- Onions"
        type = block_to_block_type(markdown)
        self.assertEqual(type,correct)

        correct = block_type_paragraph
        markdown = "* Carrots\n- Tomatoes\n* Onions"
        type = block_to_block_type(markdown)
        self.assertEqual(type,correct)
    
    def test_heading_block_id(self):
        correct = block_type_heading
        
        markdown = "### Play of the Century"
        type = block_to_block_type(markdown)
        self.assertEqual(type,correct)
        
        markdown = "###### Play of the Century"
        type = block_to_block_type(markdown)
        self.assertEqual(type,correct)

        correct = block_type_paragraph
        markdown = "######### Play of the Century"
        type = block_to_block_type(markdown)
        self.assertEqual(type,correct)
    
    def test_code_block_id(self):
        correct = block_type_code
        
        markdown = "```print(Hello World)```"
        type = block_to_block_type(markdown)
        self.assertEqual(type,correct)

        markdown = "```print(I come first!)\nprint(Hello World)```"
        type = block_to_block_type(markdown)
        self.assertEqual(type,correct)

    def test_quote_block_id(self):
        correct = block_type_quote
        
        markdown = ">Friends, Romans, countrymen, lend me your ears"
        type = block_to_block_type(markdown)
        self.assertEqual(type,correct)

        markdown = ">>Friends, Romans, countrymen, lend me your ears<>"
        type = block_to_block_type(markdown)
        self.assertEqual(type,correct)
    
    def test_basic_blocks(self):
        markdown = "# This is a heading\n\nThis is a paragraph of text. It has some **bold** and *italic* words inside of it.\n\n* This is the first list item in a list block\n* This is a list item\n* This is another list item"
        blocks = markdown_to_blocks(markdown)
        correct = ['# This is a heading', 
                   'This is a paragraph of text. It has some **bold** and *italic* words inside of it.', 
                   '* This is the first list item in a list block\n* This is a list item\n* This is another list item']
        self.assertListEqual(blocks,correct)

    def test_blocks_with_extra_spaces(self):
        markdown = "# This is a heading   \n\n   This is a paragraph of text. It has some **bold** and *italic* words inside of it.   \n\n* This is the first list item in a list block\n* This is a list item\n* This is another list item"
        blocks = markdown_to_blocks(markdown)
        correct = ['# This is a heading', 
                   'This is a paragraph of text. It has some **bold** and *italic* words inside of it.', 
                   '* This is the first list item in a list block\n* This is a list item\n* This is another list item']
        self.assertListEqual(blocks,correct)

    def test_blocks_with_extra_newlines(self):
        # Three new lines
        markdown = "# This is a heading\n\n\nThis is a paragraph of text. It has some **bold** and *italic* words inside of it.\n\n* This is the first list item in a list block\n* This is a list item\n* This is another list item"
        blocks = markdown_to_blocks(markdown)
        correct = ['# This is a heading', 
                   'This is a paragraph of text. It has some **bold** and *italic* words inside of it.', 
                   '* This is the first list item in a list block\n* This is a list item\n* This is another list item']
        self.assertListEqual(blocks,correct)

        # Four New lines
        markdown = "# This is a heading\n\n\n\nThis is a paragraph of text. It has some **bold** and *italic* words inside of it.\n\n\n\n* This is the first list item in a list block\n* This is a list item\n* This is another list item"
        blocks = markdown_to_blocks(markdown)
        correct = ['# This is a heading', 
                   'This is a paragraph of text. It has some **bold** and *italic* words inside of it.', 
                   '* This is the first list item in a list block\n* This is a list item\n* This is another list item']
        self.assertListEqual(blocks,correct)

    def test_blocks_with_everything(self):
        markdown = "# This is a heading   \n\n\n\n   This is a paragraph of text. It has some **bold** and *italic* words inside of it.  \n\n\n   * This is the first list item in a list block\n* This is a list item\n* This is another list item"
        blocks = markdown_to_blocks(markdown)
        correct = ['# This is a heading', 
                   'This is a paragraph of text. It has some **bold** and *italic* words inside of it.', 
                   '* This is the first list item in a list block\n* This is a list item\n* This is another list item']
        self.assertListEqual(blocks,correct)

if __name__ == '__main__':
    unittest.main()