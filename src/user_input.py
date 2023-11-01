from PIL import Image


def get_photo_from_user():
    filepath = input("Please enter the file path of the image: ")
    if is_valid_image(filepath):
        print("What do you want to do with this image?")
    else:
        print("Invalid image file")


def is_valid_image(filepath):
    try:
        img = Image.open(filepath)
        img.close()
        return True
    except Exception as e:
        return False
