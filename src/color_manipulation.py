import cv2
import numpy as np


def adjust_color_balance(input_image_path, output_image_path):
    img = cv2.imread(input_image_path)
    print("Adjust the color balance by specifying factors for red, green, and blue channels")

    red_factor = input("Please insert factor for red: ")
    if not is_valid_factor(red_factor):
        print("You have selected an invalid character.")
        return False
    red_factor = float(red_factor)

    blue_factor = input("Please insert factor for blue: ")
    if not is_valid_factor(blue_factor):
        print("You have selected an invalid character.")
        return False
    blue_factor = float(blue_factor)

    green_factor = input("Please insert factor for green: ")
    if not is_valid_factor(green_factor):
        print("You have selected an invalid character.")
        return False
    green_factor = float(green_factor)

    img[:, :, 0] = np.clip(img[:, :, 0] * blue_factor, 0, 255)  # Adjust blue channel
    img[:, :, 1] = np.clip(img[:, :, 1] * green_factor, 0, 255)  # Adjust green channel
    img[:, :, 2] = np.clip(img[:, :, 2] * red_factor, 0, 255)  # Adjust red channel
    cv2.imwrite(output_image_path, img)
    return True


def is_valid_factor(factor):
    try:
        float(factor)
        return True
    except Exception:
        return False
