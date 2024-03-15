import unittest


from textnode import TextNode
from textnode import extract_markdown_images, extract_markdown_links


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



    def test_extract_markdown_images(text):
        text = "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and ![another](https://i.imgur.com/dfsdkjfd.png)"
        result = [("image", "https://i.imgur.com/zjjcJKZ.png"), ("another", "https://i.imgur.com/dfsdkjfd.png")]
        assert extract_markdown_images(text) == result

    def test_extract_markdown_links(text):
        text = "This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)"
        result = [("link", "https://www.example.com"), ("another", "https://www.example.com/another")]
        assert extract_markdown_links(text) == result






if __name__ == "__main__":
    unittest.main()
