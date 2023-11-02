import os
from src.grayscale_conversion import convert_to_grayscale
from src.blurring import apply_blur
from src.sharpening import apply_sharpening
from src.edge_detection import apply_edge_detection

DICT_MENU = {1: {"name": "Grayscale Conversion",
                 "function": convert_to_grayscale,
                 "file_name": "gray"},
             2: {"name": "Blurring",
                 "function": apply_blur,
                 "file_name": "blur"},
             3: {"name": "Sharpening",
                 "function": apply_sharpening,
                 "file_name": "sharp"},
             4: {"name": "Edge Detection",
                 "function": apply_edge_detection,
                 "file_name": "edge_detection"},
             5: {"name": "Color Manipulation",
                 "function": None,
                 "file_name": "color_manipulation"},
             6: {"name": "Colorize Black and White Photos",
                 "function": None,
                 "file_name": "color"}}


def print_menu():
    print("What do you want to do with the image? Please select a number:\n")
    for i in DICT_MENU.keys():
        print(f"For {DICT_MENU[i]['name']} please type {i}")


def apply_user_choice(user_choice, image_path):
    output_image_path = get_output_image_file_path(user_choice, image_path)
    result = DICT_MENU[user_choice]["function"](image_path, output_image_path)
    return result


def get_output_image_file_path(user_choice, image_path):
    image_file_name = os.path.basename(image_path).split('.')
    output_image_file_name = image_file_name[0] + "_" + DICT_MENU[user_choice]["file_name"] + "." + image_file_name[1]
    directory = os.path.dirname(image_path)
    return directory + "/" + output_image_file_name
