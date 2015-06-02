import cv2
import math
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('whale.jpg', 0)
# sobel_x = np.matrix([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
# sobel_y = np.matrix([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])
gabor = np.matrix([[1, -4, 6, -4, 1], [-4, 16, -24, 16, -4], [6, -24, 37, -24, 6], [-4, 16, -24, 16, -4], [1, -4, 6, -4, 1]])

# conv_x = cv2.filter2D(img, cv2.CV_64F, sobel_x)
# conv_y = cv2.filter2D(img, cv2.CV_64F, sobel_y)
conv = cv2.filter2D(img, cv2.CV_64F, gabor)

# kernel = np.ones(3)
# opening = cv2.morphologyEx(conv_y, cv2.MORPH_OPEN, kernel)
# lapl = cv2.Laplacian(img, cv2.CV_64F)

cv2.imshow('gabor', conv)
cv2.waitKey(0)