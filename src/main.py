from textnode import TextNode, TextType
from website import copy_contents, generate_pages_recursive
import sys

def main():
    basepath = sys.argv[0] if len(sys.argv) > 0 else "/"
    copy_contents("static", "public")
    generate_pages_recursive("content", "template.html", "docs", basepath)

if __name__ == "__main__":
    main()
