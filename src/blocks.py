from enum import Enum
import re

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered list"
    ORDERED_LIST = "ordered list"

def markdown_to_blocks(markdown):
    return list(filter(lambda b:len(b) > 0,map(lambda s: s.strip(" \n"),markdown.split("\n\n"))))

def block_to_block_type(block):
    if re.match(r"#{1,6} ", block):
        return BlockType.HEADING
    elif re.match(r"^```[^`]*```$", block):
        return BlockType.CODE
    
    split_block = list(map(str.strip,block.split("\n")))

    if all(re.match(r">",b) for b in split_block):
        return BlockType.QUOTE
    elif all(re.match(r"- ",b) for b in split_block):
        return BlockType.UNORDERED_LIST
    
    block_zip = zip(split_block,range(1,len(split_block)+1))

    if all(re.match(rf"{n}. ",b) for b,n in block_zip):
        return BlockType.ORDERED_LIST
    else:
        return BlockType.PARAGRAPH
    
def main():
    md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""
    print(markdown_to_blocks(md))
    print(block_to_block_type(markdown_to_blocks(md)[0]))

if __name__ == "__main__":
    main()