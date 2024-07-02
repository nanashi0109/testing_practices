from src.practice_2.Library import Library
import unittest


class TestLibrary(unittest.TestCase):
    def setUp(self):
        self.library = Library()

    def test_add_book(self):
        self.library.add_book("Book A")
        self.assertTrue(self.library.find_book("Book A"))
        self.assertFalse(self.library.find_book("Book B"))

    def test_remove_book(self):
        self.library.add_book("Book A")
        self.library.add_book("Book A")
        self.library.remove_book("Book A")
        self.assertTrue(self.library.find_book("Book A"))
        self.library.remove_book("Book A")
        self.assertFalse(self.library.find_book("Book A"))
        self.library.remove_book("Book B")

    def test_find_book(self):
        self.library.add_book("Book A")
        self.assertTrue(self.library.find_book("Book A"))
        self.library.remove_book("Book A")
        self.assertFalse(self.library.find_book("Book A"))


if __name__ == '__main__':
    unittest.main()
