import cv2

WEIGHT_RED = 0.299
WEIGHT_GREEN = 0.587
WEIGHT_BLUE = 0.114


def convert_to_grayscale(input_image_path, output_image_path):
    img = cv2.imread(input_image_path)
    r, g, b = img[:, :, 0], img[:, :, 1], img[:, :, 2]
    gray_img = (WEIGHT_RED * r + WEIGHT_GREEN * g + WEIGHT_BLUE * b)
    cv2.imwrite(output_image_path, gray_img)
    return True
