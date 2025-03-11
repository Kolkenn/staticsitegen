import re
from textnode import TextNode,TextType

def text_to_textnodes(text):
    text_node = [TextNode(text,TextType.TEXT)]
    images_processed = split_nodes_image(text_node)
    links_processed = split_nodes_link(images_processed)
    bold_processed = split_nodes_delimiter(links_processed,"**",TextType.BOLD)
    italic_processed = split_nodes_delimiter(bold_processed,"_",TextType.ITALIC)
    code_processed = split_nodes_delimiter(italic_processed,"`",TextType.CODE)
    return code_processed

def split_nodes_delimiter(old_nodes,delimiter,text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        sections = old_node.text.split(delimiter)
        if len(sections) % 2 == 0:
            # No closing delimiter
            raise ValueError(f"No closing '{delimiter}' delimiter found.")
        for i in range(len(sections)):
            if sections[i] == "":
                # Empty String, skip.
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i],TextType.TEXT,None))
            else:
                split_nodes.append(TextNode(sections[i],text_type))
        new_nodes.extend(split_nodes)
    return new_nodes

def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        # Check if Text_Type is correct. (Only process Text nothing else)
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        
        # Check for images in the text. - BASE CASE for recursion
        images_found = extract_markdown_images(old_node.text)
        if len(images_found) == 0:
            # No images in this text.
            new_nodes.append(old_node)
            continue
        
        # Process images found
        alt_text = images_found[0][0]
        url = images_found[0][1]
        split_nodes = []
        sections = old_node.text.split(f"![{alt_text}]({url})",maxsplit=1)
        
        if sections[0] != "":
            split_nodes.append(TextNode(sections[0],TextType.TEXT,None))
        split_nodes.append(TextNode(alt_text,TextType.IMAGE,url))
        if sections[1] != "":
            split_nodes.append(TextNode(sections[1],TextType.TEXT,None))
        
        new_nodes.extend(split_nodes_image(split_nodes)) # Recurse
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        # Check if Text_Type is correct. (Only process Text nothing else)
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        
        # Check for links in the text. - BASE CASE for recursion
        links_found = extract_markdown_links(old_node.text)
        if len(links_found) == 0:
            # No links in this text.
            new_nodes.append(old_node)
            continue
        
        # Process links found
        alt_text = links_found[0][0]
        url = links_found[0][1]
        split_nodes = []
        sections = old_node.text.split(f"[{alt_text}]({url})",maxsplit=1)
        
        if sections[0] != "":
            split_nodes.append(TextNode(sections[0],TextType.TEXT,None))
        split_nodes.append(TextNode(alt_text,TextType.LINK,url))
        if sections[1] != "":
            split_nodes.append(TextNode(sections[1],TextType.TEXT,None))

        new_nodes.extend(split_nodes_link(split_nodes)) # Recurse
    return new_nodes

def extract_markdown_images(text):
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)",text)

def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)",text)