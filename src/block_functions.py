block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_olist = "ordered_list"
block_type_ulist = "unordered_list"

def markdown_to_blocks(markdown_line):
    blocks = markdown_line.split("\n\n")
    valid_blocks = []
    for i in range(len(blocks)):
        if blocks[i] == "":
            continue
        valid_blocks.append(blocks[i].strip('\n '))
    return valid_blocks

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
                    return block_type_heading
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

