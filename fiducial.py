import cv2
import numpy as np
import matplotlib as plt
import math

from gopro2_calibration import *

cap = cv2.VideoCapture(0)
lines_lastFiveFrames = [0, 0, 0, 0, 0]

while(True):
	ret, frame = cap.read()
	# dst = cv2.undistort(frame, mtx, dist, None, newcameramtx)
	# x,y,w,h = roi
	# frame = dst[y:y+h, x:x+w]
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	ret, thresh = cv2.threshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 11, 2)
	ret, thresh = cv2.threshold(thresh, 150, 255, cv2.THRESH_BINARY)
	opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, np.ones(7))

	contours, hierarchy = cv2.findContours(opening, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
	contours_only = np.zeros(gray.shape, np.float32)
	contours_only = cv2.cvtColor(contours_only, cv2.COLOR_GRAY2BGR)
	if contours != None:
		cv2.drawContours(contours_only, contours, -1, (255,255,255), 3)
	contours_only = cv2.cvtColor(contours_only, cv2.COLOR_BGR2GRAY)
	contours_only = contours_only.astype(np.uint8)

	canny = cv2.Canny(gray, 400, 600, 3)
	res = cv2.bitwise_and(canny, contours_only)

	lines = cv2.HoughLines(res, 0.5, np.pi/360, 30)
	if lines != None:
		print len(lines[0])
		for rho, theta in lines[0]:
			a = np.cos(theta)
			b = np.sin(theta)
			x0 = a*rho
			y0 = b*rho
			x1 = int(x0 + 1000*(-b))
			y1 = int(y0 + 1000*(a))
			x2 = int(x0 - 1000*(-b))
			y2 = int(y0 - 1000*(a))
			cv2.line(gray, (x1,y1), (x2,y2), (0,0,255), 3)
		lines_lastFiveFrames.append(lines[0])
		lines_lastFiveFrames.pop(0)

	if lines != None and len(lines[0]) > 1:
		for i in range(len(lines[0])):
			for j in range(len(lines[0])):
				if 

	# lines = cv2.HoughLinesP(res, 1, np.pi/180, 70, 10, 10)
	# if lines != None:
	# 	for x1, y1, x2, y2 in lines[0]:
	# 	    cv2.line(gray, (x1,y1), (x2,y2), (0,255,0), 2)


	cv2.imshow('res', res)
	cv2.imshow('final image', gray)

	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cap.release
cv2.destroyAllWindows()