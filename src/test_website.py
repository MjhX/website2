import unittest

from website import extract_title


class TestWebsite(unittest.TestCase):
    def test_extract_title_1(self):
        md = "# Hello"
        title = extract_title(md)
        self.assertEqual(title,"Hello")

    def test_extract_title_2(self):
        md = """
test
# Hello World
"""
        title = extract_title(md)
        self.assertEqual(title,"Hello World")
        
    def test_extract_title_3(self):
        md = """
## false header
test
# Hello Real Header
"""
        title = extract_title(md)
        self.assertEqual(title,"Hello Real Header")

if __name__ == "__main__":
    unittest.main()
