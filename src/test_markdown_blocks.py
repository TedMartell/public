import unittest
from markdown_blocks import (
    markdown_to_blocks,
)

from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_image,
    text_type_link
)


class TestInlineMarkdown(unittest.TestCase):
    def test_markdown_to_block(self):
        text = ("                 # This is a heading\n" 
                "  \n"
                "\n"
                "This is a paragraph of text. It has some **bold** and *italic* words inside of it.                \n"
                "\n"
                "            * This is a list item\n"
                "* This is another list item\n")
        result = ["# This is a heading",
                  "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
                  "* This is a list item\n* This is another list item"]
        self.assertEqual(markdown_to_blocks(text), result)


























    if __name__ == "__main__":
        unittest.main()