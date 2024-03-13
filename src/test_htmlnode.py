import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode("1", "2", "3", {"href":"google"})
        self.props = ' href="google"'
        self.assertEqual(node.props_to_html(), self.props)

    def test__mult_props_to_html(self):
        node = HTMLNode("1", "2", "3", {"Olli":"Homo", "Craiso":"Homo"})
        self.props = ' Olli="Homo"'' Craiso="Homo"'
        self.assertEqual(node.props_to_html(), self.props)
   
    def test__empty_props_to_html(self):
        node = HTMLNode("1", "2", "3", {})
        dict = ""
        self.assertEqual(node.props_to_html(), dict)

    def test_to_html(self):
        node = LeafNode("p", "Click",{"href":"google"})
        text = '<p href="google">Click</p>'
        self.assertEqual(node.to_html(), text)

    def test_to_html_props_none(self):
        node = LeafNode("p", "Click", None)
        text = '<p>Click</p>'
        self.assertEqual(node.to_html(), text)

    def test_to_html_tags_none(self):
        node = LeafNode(None, "Click",{"href":"google"})
        text = 'Click'
        self.assertEqual(node.to_html(), text)

    def test_to_html_value_none(self):
        node = LeafNode("p", None,{"href":"google"})
        self.assertRaises(ValueError, node.to_html)

    def test_to_html_parent(self):
        node = ParentNode(
    "p",
    [
        LeafNode("b", "Bold text", None),
        LeafNode(None, "Normal text", None),
        LeafNode("i", "italic text", None),
        LeafNode(None, "Normal text", None),
    ],
)
        text = "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
        self.assertEqual(node.to_html(), text)

    

    def test_to_html_tag_none(self):
        node = ParentNode(None, LeafNode("b", "Bold text", None))
        self.assertRaises(ValueError, node.to_html)

    def test_to_html_children_none(self):
        node = ParentNode("p", [])
        self.assertRaises(ValueError, node.to_html)


    
    



if __name__ == "__main__":
    unittest.main()