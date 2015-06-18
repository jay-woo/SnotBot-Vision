import cv2
import numpy as np
import matplotlib as plt
import math

cap = cv2.VideoCapture(1)

while(True):
	ret, frame = cap.read()
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	# blur = cv2.GaussianBlur(gray, (5,5), 0)
	# canny = cv2.Canny(blur, 150, 200)

	corners = cv2.cornerHarris(gray, 2, 3, 0.01)
	corners = cv2.dilate(corners, None)
	gray[corners > 0.01*corners.max()] = 255

	# lines = cv2.HoughLinesP(canny, 1, np.pi/180, 100, 1, 0)
	# if lines != None:
	# 	for x1,y1,x2,y2 in lines[0]:
	# 		cv2.line(gray,(x1,y1),(x2,y2),(0,255,0),2)

	# cv2.imshow('magnitude', gray)
	cv2.imshow('canny', gray)	

	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()