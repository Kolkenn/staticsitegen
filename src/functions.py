import re
from textnode import TextNode,TextType

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