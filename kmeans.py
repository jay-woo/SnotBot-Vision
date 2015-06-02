import numpy as np
import cv2

img = cv2.imread('whale2.jpeg')
Z = img.reshape(-1, 3)
Z = np.float32(Z)

criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
K = 4
ret,label,center = cv2.kmeans(Z, K, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

center = np.uint8(center)
res = center[label.flatten()]
res2 = res.reshape((img.shape))

cv2.imshow('res2', res2)
cv2.waitKey(0)
cv2.destroyAllWindows()