class HTMLNode:
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise(NotImplementedError)
    
    def props_html(self):
        string = ""
        dict_keys = self.props.keys()
        for value in dict_keys:
            string += str(value)
            string += "='"
            string += self.props.get(str(value))
            string += "' "
        return string
    
    def __repr__(self):
        return (f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})")

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props = None):
        self.tag = tag
        self.value = value
        self.props = props
        super().__init__(self.tag, self.value, None, self.props)
    
    def to_html(self):
        string = ""
        if(self.value == None):
            raise(ValueError)
        if(self.tag == None):
            return str(self.value)
        if(self.props == None):
            string += f"<{self.tag}>{self.value}</{self.tag}>"
        else:
            props = self.props_html()
            string += f"<{self.tag} {props}>{self.value}</{self.tag}>"
        return string

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props = None):
        self.tag = tag
        self.children = children
        self.props = props
        super().__init__(self.tag, None, self.children, self.props)
    
    def to_html(self):
        string = ""
        if(self.tag == None):
            raise(ValueError)
        if(self.children == None):
            raise(ValueError)
        for child in self.children:
            string += child.to_html()
        return f"<{self.tag}>{string}</{self.tag}>"

