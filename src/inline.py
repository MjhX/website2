from textnode import TextNode, TextType
import re

# WARNING: Some edge cases aren't covered
# If the final part breaks again, check this part
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    def split_node_delimiter(old_node):
        if old_node.text_type != TextType.TEXT:
            return [old_node]
        nodes = old_node.text.split(delimiter)
        even_or_odd = list(map(lambda x:x%2, range(len(nodes))))
        zipped_nodes = zip(nodes, even_or_odd)
        return list(map(lambda x: TextNode(x[0],text_type if x[1] != 0 else TextType.TEXT), zipped_nodes))
    return sum(map(split_node_delimiter,old_nodes),[])

def extract_markdown_images(text):
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)",text)

def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)",text)

def split_nodes_general(old_nodes, pattern, text_type):
    def split_node_general(old_node):
        if old_node.text_type != TextType.TEXT:
            return [old_node]
        ret = []
        split_list = list(re.split(pattern, old_node.text))
        while len(split_list) > 0:
            text = split_list.pop(0)
            if len(text) > 0:
                ret.append(TextNode(text, TextType.TEXT))
            if len(split_list) >= 2:
                title = split_list.pop(0)
                url = split_list.pop(0)
                ret.append(TextNode(title, text_type, url))
        return ret
    return sum(list(map(split_node_general,old_nodes)),[])

def split_nodes_image(old_nodes):
    return split_nodes_general(old_nodes, r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", TextType.IMAGE)

def split_nodes_link(old_nodes):
    return split_nodes_general(old_nodes, r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", TextType.LINK)

def text_to_textnodes(text):
    first_node = [TextNode(text,TextType.TEXT)]
    return split_nodes_image(
        split_nodes_link(
            split_nodes_delimiter(
                split_nodes_delimiter(
                    split_nodes_delimiter(first_node,
                                          "**", TextType.BOLD),
                                          "_", TextType.ITALIC),
                                          "`", TextType.CODE)
        )
    )

def main():
    print(split_nodes_link([TextNode(
        "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
        TextType.TEXT,
    )]))

if __name__ == "__main__":
    main()