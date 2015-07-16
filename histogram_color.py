import cv2
import numpy as np
from matplotlib import pyplot as plt

cap = cv2.VideoCapture(0)
h1, = plt.plot([], [], label='b')
h2, = plt.plot([], [], label='g')
h3, = plt.plot([], [], label='r')

while(True):
    ret, frame = cap.read()

# ret, th_h = cv2.threshold(h, 225, 255, cv2.THRESH_TOZERO_INV)
# ret, th_s = cv2.threshold(s, 225, 255, cv2.THRESH_TOZERO_INV)
# ret, th_v = cv2.threshold(v, 225, 255, cv2.THRESH_TOZERO_INV)

    hist_b = cv2.calcHist([frame], [0], None, [256], [0,256])
    hist_g = cv2.calcHist([frame], [1], None, [256], [0,256])
    hist_r = cv2.calcHist([frame], [2], None, [256], [0,256])
 
# hist_b = [i for [i] in hist_b]
# hist_g = [i for [i] in hist_g]
# hist_r = [i for [i] in hist_r]
# 
# cutoff_b = max(hist_b[1:256]) * 0.4
# cutoff_g = max(hist_g[1:256]) * 0.4
# cutoff_r = max(hist_r[1:256]) * 0.4
# 
# order_b = np.argsort(hist_b)
# order_g = np.argsort(hist_g)
# order_r = np.argsort(hist_r)
# 
# ignore_b = [i for i in order_b if hist_b[i] > cutoff_b]
# ignore_g = [i for i in order_g if hist_g[i] > cutoff_g]
# ignore_r = [i for i in order_r if hist_r[i] > cutoff_r]

# ret, otsu_b = cv2.threshold(th_b, 0, 255, cv2.THRESH_TOZERO+cv2.THRESH_OTSU)
# ret, otsu_g = cv2.threshold(th_g, 0, 255, cv2.THRESH_TOZERO+cv2.THRESH_OTSU)
# ret, otsu_r = cv2.threshold(th_r, 0, 255, cv2.THRESH_TOZERO+cv2.THRESH_OTSU)

    h1.set_ydata(hist_b)
    h1.set_xdata(range(256))
    h2.set_ydata(hist_g)
    h2.set_xdata(range(256))
    h3.set_ydata(hist_r)
    h3.set_xdata(range(256))
    
    plt.draw()
   
    if cv2.waitKey(1) & 0xFF == 27:
        break

# frame = cv2.merge((otsu_b, otsu_g, otsu_r))
# cv2.namedWindow('image')
# while(True):
#     cv2.imshow('image', frame)
# 
#     if cv2.waitKey(1) & 0xFF == 27:
#         break
