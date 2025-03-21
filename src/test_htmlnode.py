import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

class TestTextNode(unittest.TestCase):
    def test_props_html_func(self):
        dict = {"href": "https://www.google.com", "target": "_blank"}
        string = "href='https://www.google.com' target='_blank' "
        node = HTMLNode("<p>", "this is some text", None, dict)
        value = node.props_html()
        self.assertEqual(value, string)

    def test_values(self):
        node = HTMLNode(
            "div",
            "I wish I could read",
        )
        self.assertEqual(
            node.tag,
            "div",
        )
        self.assertEqual(
            node.value,
            "I wish I could read",
        )
        self.assertEqual(
            node.children,
            None,
        )
        self.assertEqual(
            node.props,
            None,
        )

    def test_print(self):
        dict = {"href": "https://www.google.com", "target": "_blank"}
        node = HTMLNode("<p>", "this is some text", None, dict)
        expected_string = "HTMLNode(<p>, this is some text, None, {'href': 'https://www.google.com', 'target': '_blank'})"
        print(node)
        x = node.__repr__()
        self.assertEqual(x, expected_string)
    
    def test_empty_node(self):
        node = HTMLNode()
        print(node)
        expected_string = "HTMLNode(None, None, None, None)"
        self.assertEqual(node.__repr__(), expected_string)
    
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    
    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Hello, world!", {"href": "www.ashley-is-cool.com"})
        self.assertEqual(node.to_html(), "<a href='www.ashley-is-cool.com' >Hello, world!</a>")
    
    def test_leaf_to_html_div(self):
        node = LeafNode("div", "Hello, world!", {"href": "www.ashley-is-cool.com"})
        self.assertEqual(node.to_html(), "<div href='www.ashley-is-cool.com' >Hello, world!</div>")

    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")
    
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
    
    def test_to_html_many_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
        )
    
    def test_headings(self):
        node = ParentNode(
            "h2",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<h2><b>Bold text</b>Normal text<i>italic text</i>Normal text</h2>",
        )
    
    def test_to_html_with_no_children(self):
        parent_node = ParentNode("div", None)
        self.assertRaises(ValueError, parent_node.to_html)

    def test_to_html_with_no_tags(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode(None, [child_node])
        self.assertRaises(ValueError, parent_node.to_html)


if __name__ == "__main__":
    unittest.main()