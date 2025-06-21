import re
from blocks import BlockType, markdown_to_blocks, block_to_block_type
from htmlnode import ParentNode, LeafNode
from textnode import TextType, TextNode, text_node_to_html_node
from inline import text_to_textnodes

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = list(map(process_blocks, blocks))
    return ParentNode("div", children)

def process_blocks(block):
    bt = block_to_block_type(block)
    match bt:
        case BlockType.QUOTE:
            return make_htmlnode_quote(block)
        case BlockType.UNORDERED_LIST:
            return make_htmlnode_unordered_list(block)
        case BlockType.ORDERED_LIST:
            return make_htmlnode_ordered_list(block)
        case BlockType.CODE:
            return make_htmlnode_code(block)
        case BlockType.HEADING:
            return make_htmlnode_heading(block)
        case _:
            return make_htmlnode_paragraph(block)

def make_htmlnode_quote(block):
    formatted_blocks = "\n".join(list(map(lambda b: re.sub(r"^>","",b),block.split("\n")))).split("\n\n")
    children = list(map(process_blocks, formatted_blocks))
    return ParentNode("blockquote", children)

def make_htmlnode_unordered_list(block):
    split_blocks = list(map(lambda b: re.sub(r"^- ","",b),block.split("\n")))
    li_children = list(map(lambda b: ParentNode("li",text_to_html_nodes(b)),split_blocks))
    return ParentNode("ul", li_children)

def make_htmlnode_ordered_list(block):
    split_blocks = list(map(lambda b: re.sub(r"^[1-9][0-9]*\. ","",b),block.split("\n")))
    li_children = list(map(lambda b: ParentNode("li",text_to_html_nodes(b)),split_blocks))
    return ParentNode("ol", li_children)

def make_htmlnode_code(block):
    value = re.sub(r"^```", "", block)
    value = re.sub(r"```$", "", value).lstrip("\n ")
    return ParentNode("pre", [LeafNode("code",value)])

def make_htmlnode_heading(block):
    parts = block.split(" ",1)
    return ParentNode(f"h{len(parts[0])}", text_to_html_nodes(parts[1]))

def make_htmlnode_paragraph(block):
    return ParentNode("p",text_to_html_nodes(block.replace("\n"," ")))

def text_to_html_nodes(text):
    return list(map(text_node_to_html_node,text_to_textnodes(text)))

def main():
    md2 = """
>**test1**
>_test2_
>
>test3

>test4
"""
    node2 = markdown_to_html_node(md2)
    html2 = node2.to_html()
    print(html2)



if __name__ == "__main__":
    main()