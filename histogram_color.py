import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('whale_zoomed.jpg')
color = ('b', 'g', 'r')

# for i, col in enumerate(color):
# 	hist = cv2.calcHist([img], [i], None, [256], [0, 256])
# 	plt.plot(hist, color = col)

# plt.show()

thresh = cv2.inRange(img, np.array([125, 100, 75]), np.array([175, 150, 125]))
new_img = cv2.bitwise_and(img, img, mask=thresh)

cv2.imshow('new image', new_img)
cv2.waitKey(0)