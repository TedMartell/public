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
        try:
            node.to_html()
        except ValueError:
            pass


    
    



if __name__ == "__main__":
    unittest.main()