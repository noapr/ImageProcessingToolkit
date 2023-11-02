import cv2
import numpy as np

LAPLACIAN_KERNEL = np.array([[0, -1, 0],
                             [-1, 5, -1],
                             [0, -1, 0]])


def apply_sharpening(input_image_path, output_image_path):
    img = cv2.imread(input_image_path)
    sharpened_img = cv2.filter2D(img, -1, LAPLACIAN_KERNEL)
    cv2.imwrite(output_image_path, sharpened_img)
    return True
