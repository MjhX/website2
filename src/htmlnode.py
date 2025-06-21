class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    def __repr__(self):
        return f"HTML Node({self.tag}, {self.value}, {self.children}, {self.props})"
    def to_html(self):
        raise NotImplementedError("Not implemented: override with a child class")
    def props_to_html(self):
        if self.props == None:
            return ""
        return "".join(map(lambda t: " "+t[0]+'="'+t[1]+'"', self.props.items()))
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)
    def to_html(self):
        if self.value == None:
            raise ValueError("All leaf nodes must have a value")
        if self.tag == None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
    def to_html(self):
        if self.tag == None:
            raise ValueError("All parent nodes must have a tag")
        if self.children == None:
            raise ValueError("All parent nodes must have children")
        return f"<{self.tag}{self.props_to_html()}>{"".join(map(lambda c: c.to_html(),self.children))}</{self.tag}>"