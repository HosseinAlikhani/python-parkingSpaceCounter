import numpy as np
import cv2

cap = cv2.VideoCapture('./carPark.mp4')

while True:
    ret, frame = cap.read()
    if ret :
        cv2.imshow("Image", frame)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

cv2.destroyAllWindows()