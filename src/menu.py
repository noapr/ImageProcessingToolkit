DICT_MENU = {1: {"name": "Grayscale Conversion",
                 "function": None},
             2: {"name": "Blurring",
                 "function": None},
             3: {"name": "Sharpening",
                 "function": None},
             4: {"name": "Edge Detection",
                 "function": None},
             5: {"name": "Color Manipulation",
                 "function": None},
             6: {"name": "Colorize Black and White Photos",
                 "function": None}}


def print_menu():
    print("What do you want to do with the image? Please select a number:\n")
    for i in DICT_MENU.keys():
        print(f"For {DICT_MENU[i]['name']} please type {i}")


def apply_user_choice(user_choice, image_path):
    result = DICT_MENU[user_choice]["function"](image_path)
