from textnode import TextNode,TextType

def split_nodes_delimiter(old_nodes,delimiter,text_type):
    new_nodes = []
    for nodes in old_nodes:
        if nodes.text_type != TextType.TEXT:
            new_nodes.append(nodes)
        else:
            split_text = nodes.text.split(delimiter)
            if len(split_text) == 3:
                new_nodes.append(TextNode(split_text[0],TextType.TEXT))
                new_nodes.append(TextNode(split_text[1],text_type))
                new_nodes.append(TextNode(split_text[2],TextType.TEXT))
            elif len(split_text) == 2:
                # No closing delimiter
                raise ValueError(f"No closing '{delimiter}' delimiter found.")
            else:
                new_nodes.append(nodes)
    return new_nodes