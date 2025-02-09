import unittest
from pathlib import Path

from htmlnode import *
from textnode import *
from block_functions import *
from inline_functions import *

class TestBlockToHtml(unittest.TestCase):
    def test_complete(self):
        md_file = Path('src/markdown_input.md').read_text()
        md_blocks = markdown_to_blocks(md_file)
        for blocks in md_blocks:
            type = block_to_block_type(blocks)
            print(f"{type}: {blocks}")
        pass

if __name__ == '__main__':
    unittest.main()