import cv2
import time
import numpy as np

cap = cv2.VideoCapture(0)
fondo = None
 
while True:

	grabbed, frame = cap.read()
 
	if not grabbed:
		break
 
	img_gris = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	img_gris = cv2.GaussianBlur(img_gris, (21, 21), 0)

	if fondo is None:
		fondo = img_gris
		continue
 
	resta = cv2.absdiff(fondo, img_gris)
 
	umbral = cv2.threshold(resta, 25, 255, cv2.THRESH_BINARY)[1]

	umbral = cv2.dilate(umbral, None, iterations=2)

	contornosimg = umbral.copy()
 
	contornos, hierarchy = cv2.findContours(contornosimg,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

	for c in contornos:
		if cv2.contourArea(c) < 500:
			continue
		(x, y, w, h) = cv2.boundingRect(c)
		cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

	cv2.imshow("Camara", frame)

	k = cv2.waitKey(10)
	time.sleep(0.015)

	if k == 27:
		break

cap.release()
cv2.destroyAllWindows()
