from textnode import TextNode, TextType
from website import copy_contents, generate_pages_recursive

def main():
    copy_contents("static", "public")
    generate_pages_recursive("content", "template.html", "public")

if __name__ == "__main__":
    main()
