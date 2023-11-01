import unittest
from src.user_input import is_valid_image


class TestIsValidImage(unittest.TestCase):

    def test_valid_image(self):
        valid_path = ["./test_data/valid_image.jpg", "./test_data/valid_image.png", "./test_data/valid_image.gif", "./test_data/valid_image.bmp"]
        for path in valid_path:
            self.assertTrue(is_valid_image(path))

    def test_invalid_image(self):
        invalid_path = "./test_data/invalid_image.txt"
        self.assertFalse(is_valid_image(invalid_path))


if __name__ == '__main__':
    unittest.main()
