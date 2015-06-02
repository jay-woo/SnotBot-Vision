import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('whale.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
new_img = cv2.inRange(gray, 100, 125)

# hist = cv2.calcHist([gray], [0], None, [256], [0, 256])

# plt.plot(hist)
# plt.show()

cv2.imshow('new image', new_img)
while True:
	k = cv2.waitKey(0)
	if k == 27: break
cv2.destroyAllWindows()