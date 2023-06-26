import numpy as np
import pickle
import cv2

cap = cv2.VideoCapture('./carPark.mp4')

while True:
    ret, frame = cap.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(frame, (3,3), 1)
    imgThreshold = cv2.adaptiveThreshold(imgBlur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 25, 16)
    imgThreshold = cv2.medianBlur(imgThreshold, 5)
    if ret :
        cv2.imshow("Image", frame)
        cv2.imshow("imgThreshold", imgThreshold)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

cv2.destroyAllWindows()