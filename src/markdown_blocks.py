from htmlnode import *
from textnode import *
from inline_markdown import *

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quite"
    OLIST = "ordered_list"
    ULIST = "unordered_list"

block_type_paragraph = "p" # Paragraph
block_type_code = "code" # Code
block_type_quote = "blockquote" # Quote
block_type_olist = "ol" # Ordered List
block_type_ulist = "ul" # Unodered_list

def markdown_to_html_node(markdown):
    html_list = []
    md_blocks = markdown_to_blocks(markdown)
    for blocks in md_blocks:
        type = block_to_block_type(blocks)
        children = text_to_children(blocks,type)
        html_list.append(ParentNode(type,children))
    return print(ParentNode("div",html_list).to_html())

def text_to_children(text,type):
    text_nodes = text_to_textnodes(text)
    children = []
    for node in text_nodes:
        children.append(text_node_to_html_node(node))
    return children

def markdown_to_blocks(markdown_line):
    blocks = markdown_line.split("\n\n")
    filtered_blocks = []
    for block in blocks:
        if block == "":
            continue
        block = block.strip()
        filtered_blocks.append(block)
    return filtered_blocks

def block_to_block_type(block):
    lines = block.split("\n")

    if block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return BlockType.HEADING
    if len(lines) > 1 and lines[0].startswith("```") and lines[-1].startswith("```"):
        return BlockType.CODE
    if block.startswith(">"):
        for line in lines:
            if not line.startswith(">"):
                return BlockType.PARAGRAPH
        return BlockType.QUOTE
    if block.startswith("- "):
        for line in lines:
            if not line.startswith("- "):
                return BlockType.PARAGRAPH
        return BlockType.ULIST
    if block.startswith("1. "):
        i = 1
        for line in lines:
            if not line.startswith(f"{i}. "):
                return BlockType.PARAGRAPH
            i += 1
        return BlockType.OLIST
    return BlockType.PARAGRAPH