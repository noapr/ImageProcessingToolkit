import unittest
from src.menu import get_output_image_file_path, DICT_MENU


class TestGetOutputImageFilePath(unittest.TestCase):

    def test_relative_path(self):
        input_image_path = "./test_data/valid_image.jpg"
        accepted_image_path = "./test_data/valid_image_" + DICT_MENU[1]["file_name"] + ".jpg"
        self.assertEquals(accepted_image_path, get_output_image_file_path(1, input_image_path))

    def test_absolute_path(self):
        input_image_path = "C:/Users/User/dev/Python/ImageProcessingToolkit/tests/test_data/valid_image.jpg"
        accepted_image_path = "C:/Users/User/dev/Python/ImageProcessingToolkit/tests/test_data/valid_image_" + DICT_MENU[1]["file_name"] + ".jpg"
        self.assertEquals(accepted_image_path, get_output_image_file_path(1, input_image_path))


if __name__ == '__main__':
    unittest.main()
