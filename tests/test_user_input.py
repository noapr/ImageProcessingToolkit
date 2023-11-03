import unittest
from src.user_input import is_valid_image, is_valid_choice
from src.menu import DICT_MENU


class TestIsValidImage(unittest.TestCase):

    def test_valid_image(self):
        valid_path = ["./test_data/valid_image.jpg", "./test_data/valid_image.png", "./test_data/valid_image.gif", "./test_data/valid_image.bmp"]
        for path in valid_path:
            self.assertTrue(is_valid_image(path))

    def test_invalid_image(self):
        invalid_path = "./test_data/invalid_image.txt"
        self.assertFalse(is_valid_image(invalid_path))


class TestIsValidChoice(unittest.TestCase):

    def test_valid_choice(self):
        valid_choices = [x for x in DICT_MENU.keys()] + [str(x) for x in DICT_MENU.keys()]
        for choice in valid_choices:
            self.assertTrue(is_valid_choice(choice))

    def test_invalid_choice(self):
        invalid_choices = ["", "fefwfeq", "22", 'q', 666, False, []]
        for choice in invalid_choices:
            self.assertFalse(is_valid_choice(choice))


if __name__ == '__main__':
    unittest.main()
