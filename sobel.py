import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('whale.jpg')
sobel = np.matrix([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
conv = cv2.filter2D(img, -1, sobel)

kernel = np.ones(3)
opening = cv2.morphologyEx(conv, cv2.MORPH_CLOSE, kernel)

plt.imshow(opening)
plt.show()