import unittest

from blocks import BlockType, markdown_to_blocks, block_to_block_type
from markdown_to_html_node import markdown_to_html_node


class TestTextNode(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    #def test_block_to_block_type_paragraph_1(self):
    #    pass

    #def test_block_to_block_type_paragraph_2(self):
    #    pass
    
    def test_block_to_block_type_heading_1(self):
        bt = block_to_block_type("#### h4 Heading")
        self.assertEqual(bt,BlockType.HEADING)
    
    def test_block_to_block_type_heading_2(self):
        bt = block_to_block_type("# ### h1 Heading")
        self.assertEqual(bt,BlockType.HEADING)
    
    def test_block_to_block_type_code_1(self):
        bt = block_to_block_type("``````")
        self.assertEqual(bt,BlockType.CODE)
    
    def test_block_to_block_type_code_2(self):
        bt = block_to_block_type("```" \
        "test" \
        "```")
        self.assertEqual(bt,BlockType.CODE)

    def test_block_to_block_type_code_3(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""
        bt = block_to_block_type((markdown_to_blocks(md)[0]))
        self.assertEqual(bt,BlockType.CODE)
    
    def test_block_to_block_type_quote_1(self):
        bt = block_to_block_type(">test")
        self.assertEqual(bt,BlockType.QUOTE)
    
    def test_block_to_block_type_quote_2(self):
        bt = block_to_block_type(">test" \
        ">test2")
        self.assertEqual(bt,BlockType.QUOTE)
    
    def test_block_to_block_type_ordered_list_1(self):
        bt = block_to_block_type("1. test" \
        "2. test2")
        self.assertEqual(bt,BlockType.ORDERED_LIST)
    
    def test_block_to_block_type_ordered_list_2(self):
        bt = block_to_block_type("1. test" \
        "2. test2" \
        "3. test3")
        self.assertEqual(bt,BlockType.ORDERED_LIST)
    
    def test_block_to_block_type_unordered_list_1(self):
        bt = block_to_block_type("- test" \
        "- test2" \
        "- test3")
        self.assertEqual(bt,BlockType.UNORDERED_LIST)
    
    def test_block_to_block_type_unordered_list_2(self):
        bt = block_to_block_type("- test")
        self.assertEqual(bt,BlockType.UNORDERED_LIST)
    
    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

    def test_quote(self):
        md = """> "I am in fact a Hobbit in all but size."
>
> -- J.R.R. Tolkien"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            """<div><blockquote>"I am in fact a Hobbit in all but size."

-- J.R.R. Tolkien</blockquote></div>""",
        )

if __name__ == "__main__":
    unittest.main()
