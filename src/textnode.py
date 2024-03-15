import re
from htmlnode import LeafNode

text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"

def extract_markdown_images(text):
    return re.findall(r"!\[(.*?)\]\((.*?)\)",text)
    
def extract_markdown_links(text):
    return re.findall(r"\[(.*?)\]\((.*?)\)",text)



class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        return self.text == other.text and self.text_type == other.text_type and self.url == other.url
    
    def __repr__(self) -> str:
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
    


    def text_node_to_html_node(text_node):
        if text_node == None:
            raise Exception("No TextNode found")
    
        if text_node.text_type == "text":
            return LeafNode(None, text_node.text, None)
        elif text_node.text_type == "bold":
            return LeafNode("b", text_node.text, None)
        elif text_node.text_type == "italic":
            return LeafNode("i", text_node.text, None)
        elif text_node.text_type == "code":
            return LeafNode("code", text_node.text, None)
        elif text_node.text_type == "link":
            return LeafNode("a", text_node.text, {"href": text_node.url})
        elif text_node.text_type == "image":
            return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
        else:
            raise Exception("Invalid text_type. text_type: " + text_node.text_type)
        


        


            
       


