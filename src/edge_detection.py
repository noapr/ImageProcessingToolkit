import cv2
import numpy as np

SOBEL_X_KERNEL = np.array([[-1, 0, 1],
                           [-2, 0, 2],
                           [-1, 0, 1]])

SOBEL_Y_KERNEL = np.array([[-1, -2, -1],
                           [0, 0, 0],
                           [1, 2, 1]])


def apply_edge_detection(input_image_path, output_image_path):
    img = cv2.imread(input_image_path, cv2.IMREAD_GRAYSCALE)
    edge_detection_x_img = cv2.filter2D(img, -1, SOBEL_X_KERNEL)
    edge_detection_y_img = cv2.filter2D(img, -1, SOBEL_Y_KERNEL)
    edge_detection_img = np.uint8(np.sqrt(edge_detection_x_img ** 2 + edge_detection_y_img ** 2))
    edge_detection_img = cv2.equalizeHist(edge_detection_img)
    cv2.imwrite(output_image_path, edge_detection_img)
    return True
