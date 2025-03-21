from enum import Enum
from htmlnode import LeafNode

class TextType(Enum):
    TEXT = "text",
    BOLD = "bold",
    ITALIC = "italic"
    CODE = "code",
    LINK = "link",
    IMAGE = "image"

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url
    
    def __eq__(self, other):
        return (
            self.text_type == other.text_type
            and self.text == other.text
            and self.url == other.url
        )
    
    def __repr__(self):
        return (f"TextNode({self.text}, {self.text_type.name}, {self.url})")

def text_node_to_html_node(text_node):
    type = text_node.text_type
    if(type == None):
        raise(ValueError)
    elif(type == TextType.TEXT):
        return LeafNode(None, text_node.text)
    elif(type == TextType.BOLD):
        return LeafNode("b", text_node.text)
    elif(type == TextType.ITALIC):
        return LeafNode("i", text_node.text)
    elif(type == TextType.CODE):
        return LeafNode("code", text_node.text)
    elif(type == TextType.LINK):
        return LeafNode("a", text_node.text, {"href": f"{text_node.url}"})
    elif(type == TextType.IMAGE):
        return LeafNode("img", "", {"src": f"{text_node.url}", "alt": f"{text_node.text}"})
    else:
        raise(ValueError)