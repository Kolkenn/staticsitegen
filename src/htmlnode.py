#The HTMLNode class will represent a "node" in an HTML document tree (like a <p> tag and its contents, or an <a> tag and its contents) and is purpose-built to render itself as HTML.
class HTMLNode():
    def __init__(self,tag=None,value=None,children=None,props=None):
        self.tag = tag # A string representing the HTML tag name (e.g. "p", "a", "h1", etc.)
        self.value = value # A string representing the value of the HTML tag
        self.children = children # A list of HTMLNode objects representing the children of this node
        self.props = props # A dictionary of key-value pairs representing the attributes of the HTML tag. For example, a link (<a> tag) might have {"href": "https://www.google.com"}

    def to_html(self):
        # Child classes will override this method to render themselves as HTML.
        raise NotImplementedError

    def props_to_html(self):
        if self.props is None:
            return ""
        temp = ""
        for keys in self.props:
            temp += f' {keys}="{self.props[keys]}"'
        return temp

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value == None:
            raise ValueError("No value provided.")
        elif self.tag == None:
            return self.value
        return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'
    
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"
    
class ParentNode(HTMLNode):
    def __init__(self, tag, children,props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag == None:
            raise ValueError("No tag provided.")
        elif self.children == None:
            raise ValueError("No children provided.")
        #Recurse through the list of children.
        def to_html_recurse(children):
            if len(children) == 0:
                return ""
            return children[0].to_html() + to_html_recurse(children[1:])        
        return f'<{self.tag}{self.props_to_html()}>{to_html_recurse(self.children)}</{self.tag}>'

    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"