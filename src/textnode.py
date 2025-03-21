from enum import Enum

class Texttype(Enum):
    NORMAL_TEXT = "",
    BOLD_TEXT = "**",
    ITALIC_TEXT = "__"
    CODE_TEXT = "`",
    LINKS = "[]()",
    IMAGES = "![]()"

class TextNode:
    def __init__(self, text, text_type, url):
        self.text = text
        self.text_type = text_type
        self.url = url
    
    def __eg__(self, textNode_a, textNode_b):
        a_elements = []
        eg = True
        for el in textNode_a:
            a_elements.insert(el)
        
        for el in textNode_b:
            if el not in textNode_b:
                eg = False
                break
        
        return eg
    
    def __repr__(self):
        print (f"TextNode({self.text}, {self.text_type.name}, {self.url})")
