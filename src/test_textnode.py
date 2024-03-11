import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold", "www.boot.dev")
        node2 = TextNode("This is a text node", "bold", "www.boot.dev")
        self.assertEqual(node, node2)
    
    def test_none(self):
        node = TextNode("This is a text node", "bold", None)
        node2 = TextNode("This is a text node", "bold", "www.boot.dev")
        self.assertNotEqual(node, node2)

    def test_dif_text(self):
        node = TextNode("This is maybe a text node", "bold", "www.boot.dev")
        node2 = TextNode("This is a text node", "bold", "www.boot.dev")
        self.assertNotEqual(node, node2)
    
    def test_dif_text_type(self):
        node = TextNode("This is a text node", "bold", "www.boot.dev")
        node2 = TextNode("This is a text node", "italic", "www.boot.dev")
        self.assertNotEqual(node, node2)

    def test_none_values(self):
        node = TextNode(None, None, None)
        self.assertIsNone(node.text)
        self.assertIsNone(node.text_type)
        self.assertIsNone(node.url)


if __name__ == "__main__":
    unittest.main()
