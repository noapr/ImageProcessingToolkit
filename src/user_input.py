from PIL import Image
from src.menu import DICT_MENU


def get_photo_from_user():
    filepath = input("Please enter the file path of the image: ")
    if is_valid_image(filepath):
        return filepath
    else:
        print("Invalid image file")
        return None


def is_valid_image(filepath):
    try:
        img = Image.open(filepath)
        img.close()
        return True
    except Exception as e:
        print(e)
        return False


def is_valid_choice(user_choice):
    try:
        num = int(user_choice)
        if num in DICT_MENU.keys():
            return True
        return False
    except Exception:
        return False
