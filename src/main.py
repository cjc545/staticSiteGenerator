from textnode import TextNode, Texttype
print("hello world")

def main():
    node = TextNode("Hello", Texttype.LINKS, "http://www.69.com")
    node.__repr__()

main()