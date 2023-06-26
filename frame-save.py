import numpy as np
import cv2

cap = cv2.VideoCapture('./carPark.mp4')


ret, frame = cap.read()
cv2.imwrite("./firstFrame.png", frame);