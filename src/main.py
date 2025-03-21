from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode, ParentNode

print("hello world")

def main():
    node = TextNode("Hello", TextType.LINK, "http://www.69.com")
    print(node)


main()