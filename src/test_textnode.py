import unittest

from textnode import TextNode, TextType, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq1(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq2(self):
        node = TextNode(str(6*8), TextType.ITALIC)
        node2 = TextNode(str(4)+str(8), TextType.ITALIC)
        self.assertEqual(node, node2)

    def test_eq3(self):
        node = TextNode(None, TextType.ITALIC)
        node2 = TextNode(None, TextType.ITALIC)
        self.assertEqual(node, node2)

    def test_neq1(self):
        node = TextNode("This is a text node", TextType.BOLD,[])
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_neq2(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_text_link(self):
        node = TextNode("This is a link node", TextType.LINK, "https://www.examplelink.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "This is a link node")
        self.assertEqual(html_node.props["href"], "https://www.examplelink.com")

    def test_text_image(self):
        node = TextNode("This is an image node", TextType.IMAGE, "https://www.exampleimage.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props["src"], "https://www.exampleimage.com")
        self.assertEqual(html_node.props["alt"], "This is an image node")


if __name__ == "__main__":
    unittest.main()
