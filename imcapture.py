import cv2
import time

cap = cv2.VideoCapture(0)

while True:
	ret, frame = cap.read()

	cv2.imshow('video', frame)

	if cv2.waitKey(1) & 0xFF == ord('q'):
		cv2.imwrite('calib10.jpg', frame)
		break

cap.release()
cv2.destroyAllWindows() 