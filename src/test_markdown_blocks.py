import unittest
from markdown_blocks import (
    markdown_to_blocks,
    block_to_block_type,
    block_type_paragraph,
    block_type_heading,
    block_type_code,
    block_type_ordered_list,
    block_type_unordered_list,
    block_type_quote,
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


    def test_block_to_block_types(self):
        block = "# heading"
        self.assertEqual(block_to_block_type(block), block_type_heading)
        block = "```\ncode\n```"
        self.assertEqual(block_to_block_type(block), block_type_code)
        block = "> quote\n> more quote"
        self.assertEqual(block_to_block_type(block), block_type_quote)
        block = "* list\n* items"
        self.assertEqual(block_to_block_type(block), block_type_unordered_list)
        block = "1. list\n2. items"
        self.assertEqual(block_to_block_type(block), block_type_ordered_list)
        block = "paragraph"
        self.assertEqual(block_to_block_type(block), block_type_paragraph)


























    if __name__ == "__main__":
        unittest.main()