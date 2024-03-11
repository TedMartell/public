import unittest

from htmlnode import HTMLNode

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


if __name__ == "__main__":
    unittest.main()