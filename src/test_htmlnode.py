import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


class TestTextNode(unittest.TestCase):
    def test_eq1(self):
        ret1 = HTMLNode(props={"href": "https://www.google.com", "target": "_blank"}).props_to_html()
        ret2 = ' href="https://www.google.com" target="_blank"'
        self.assertEqual(ret1, ret2)

    def test_eq2(self):
        ret1 = HTMLNode(props={"name": "viewport", "content": "width=device-width, initial-scale=1.0"}).props_to_html()
        ret2 = ' name="viewport" content="width=device-width, initial-scale=1.0"'
        self.assertEqual(ret1, ret2)

    def test_eq3(self):
        ret1 = HTMLNode(props={"id": "randomLinkBtn"}).props_to_html()
        ret2 = ' id="randomLinkBtn"'
        self.assertEqual(ret1, ret2)
    
    def test_leaf_to_html_p_1(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )



if __name__ == "__main__":
    unittest.main()
