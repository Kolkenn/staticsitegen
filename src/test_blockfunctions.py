import unittest
from block_functions import markdown_to_blocks,block_to_block_type

class TestBlockFunctions(unittest.TestCase):
    def test_list_block_id(self):
        correct = "Unordered List"
        
        markdown = "* Carrots\n*Tomatoes\n*Onions"
        type = block_to_block_type(markdown)
        self.assertEqual(type,correct)

    def test_heading_block_id(self):
        correct = "Heading"
        
        markdown = "### Play of the Century"
        type = block_to_block_type(markdown)
        self.assertEqual(type,correct)
    
    def test_heading_block_id(self):
        correct = "Heading"
        
        markdown = "### Play of the Century"
        type = block_to_block_type(markdown)
        self.assertEqual(type,correct)
    
    def test_code_block_id(self):
        correct = "Code"
        
        markdown = "```print(Hello World)```"
        type = block_to_block_type(markdown)
        self.assertEqual(type,correct)

        markdown = "```print(I come first!)\nprint(Hello World)```"
        type = block_to_block_type(markdown)
        self.assertEqual(type,correct)

    def test_quote_block_id(self):
        correct = "Quote"
        
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