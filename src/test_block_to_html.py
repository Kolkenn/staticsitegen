import unittest
from pathlib import Path

from block_functions import *

class TestBlockToHtml(unittest.TestCase):
    def test_complete(self):
        md_file = Path('src/markdown_input.md').read_text()
        markdown_to_html_node(md_file)

if __name__ == '__main__':
    unittest.main()