import cv2
import numpy as np

KERNEL_RANGE = [1, 100]


def apply_blur(input_image_path, output_image_path):
    img = cv2.imread(input_image_path)
    kernel_size = input(f'Please select a number between {KERNEL_RANGE[0]} and {KERNEL_RANGE[1]} for the desired blur intensity\n')
    if not is_valid_kernel_size(kernel_size):
        print("You have selected an invalid character.")
        return False
    kernel_size = int(kernel_size)
    kernel = np.ones((kernel_size, kernel_size), np.float32) / (kernel_size ** 2)  # normalized kernel
    blurred_img = cv2.filter2D(img, -1, kernel)
    cv2.imwrite(output_image_path, blurred_img)
    return True


def is_valid_kernel_size(kernel_size):
    try:
        x = int(kernel_size)
        if x in range(KERNEL_RANGE[0], KERNEL_RANGE[1] + 1):
            return True
        return False
    except Exception:
        return False
