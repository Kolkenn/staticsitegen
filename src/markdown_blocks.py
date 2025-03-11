from htmlnode import *
from textnode import *
from inline_markdown import *

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

def block_to_block_type(markdown_block):
    lines = markdown_block.split('\n')
    # Headings start with 1-6 # characters, followed by a space and then the heading text.
    if markdown_block.startswith('#'):
        heading_section = markdown_block[0:7] # Grab the first eight characters.
        for i in range(len(heading_section)):
            if i == 6: # If there are more than 6 '#' symbols, then just break that's not a heading.
                break
            if heading_section[i] != '#':
                break
            elif heading_section[i] == '#':
                if heading_section[i + 1] == ' ':
                    return f"h{i + 1}"
    # Code blocks must start with 3 backticks and end with 3 backticks.
    if markdown_block.startswith('```') and markdown_block.endswith('```'):
        return block_type_code
    # Every line in a quote block must start with a > character.
    if markdown_block.startswith('>'):
        for line in lines:
            if not line.startswith('>'):
                return block_type_paragraph
        return block_type_quote
    
    # Every line in an unordered list block must start with a * or - character, followed by a space.
    if markdown_block.startswith("* "):
        for line in lines:
            if not line.startswith("* "):
                return block_type_paragraph
        return block_type_ulist
    if markdown_block.startswith("- "):
        for line in lines:
            if not line.startswith("- "):
                return block_type_paragraph
        return block_type_ulist
    
    # Every line in an ordered list block must start with a number followed by a . character and a space. The number must start at 1 and increment by 1 for each line.
    if markdown_block.startswith("1. "):
        current_line_number = 1
        for line in lines:
            if not line.startswith(f"{current_line_number}. "):
                return block_type_paragraph
            current_line_number += 1
        return block_type_olist
    # If none of the above conditions are met, the block is a normal paragraph.
    return block_type_paragraph

