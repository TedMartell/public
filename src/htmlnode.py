class HTMLNode:
    def __init__(self, tag, value, children, props):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        text =""
        for prop in self.props:
            text+= f' {prop}="{self.props[prop]}"'
        return text
        
    def __repr__(self) -> str:
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
    
    class LeafNode(HTMLNode):
        def __init__(self, tag, value, children, props):         
            super().__init__(tag, value, children, props)
            self.children = []

    def to_html(self):
        text = ""
        if self.value == None:
            raise ValueError
        if self.tag == None:
            return f"{text}{self.value}"
        if self.props != None:
            for prop in self.props:
                text+= f' {prop}="{self.props[prop]}"'          
        return f'<{self.tag}>{text}{self.value}</{self.tag}>'
        


