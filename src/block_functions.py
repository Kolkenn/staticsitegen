
def markdown_to_blocks(markdown_line):
    blocks = markdown_line.split("\n\n")
    valid_blocks = []
    for i in range(len(blocks)):
        if blocks[i] == "":
            continue
        valid_blocks.append(blocks[i].strip('\n '))
    return valid_blocks

def block_to_block_type(markdown_block):
    # Headings start with 1-6 # characters, followed by a space and then the heading text.
    if markdown_block.startswith('#'):
        heading_section = markdown_block[0:6] # Only look at the first 7 characters
        for i in range(len(heading_section)):
            if heading_section[i] != '#':
                break
            elif heading_section[i] == '#':
                if heading_section[i + 1] == ' ':
                    return "Heading"
    # Code blocks must start with 3 backticks and end with 3 backticks.
    elif markdown_block.startswith('```') and markdown_block.endswith('```'):
        return "Code"
    # Every line in a quote block must start with a > character.
    elif markdown_block.startswith('>'):
        return "Quote"
    
    # Could be a list, split by new lines and check.
    lines = markdown_block.split('\n')
    if len(lines) > 1:
        # Every line in an unordered list block must start with a * or - character, followed by a space.
        for line in lines:
            if not line.startswith(("* ","- ")):
                break
        return "Unordered List"

    # Every line in an ordered list block must start with a number followed by a . character and a space. The number must start at 1 and increment by 1 for each line.
    # If none of the above conditions are met, the block is a normal paragraph.
    return "Normal Paragraph"

