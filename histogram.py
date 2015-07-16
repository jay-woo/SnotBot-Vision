import cv2
import numpy as np
from matplotlib import pyplot as plt

cap = cv2.VideoCapture('whales1.flv')
ret, img = cap.read()
img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
h,s,v = cv2.split(img)
ret, h = cv2.threshold(h, 120, 255, cv2.THRESH_TOZERO)
ret, s = cv2.threshold(s, 100, 255, cv2.THRESH_TOZERO)
ret, v = cv2.threshold(v, 100, 255, cv2.THRESH_TOZERO)

res = cv2.merge((h,s,v))

while(True):
    cv2.imshow('result', res)

    if cv2.waitKey(1) & 0xFF == 27:
        break
