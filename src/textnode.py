from enum import Enum

class TextType(Enum):
    TEXT = "test"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode():
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type 
        self.url = url

    def __eq__(self, other):
        if not isinstance(other,TextNode):
            raise Exception(f"{other} is not a valid TextNode object.")
        return (
            self.text is other.text 
            and self.text_type is other.text_type 
            and self.url is other.url
            )

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"