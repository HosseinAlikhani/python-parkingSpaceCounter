import numpy as np
import pickle
import cv2

cap = cv2.VideoCapture('./carPark.mp4')

with open('CarParkPos', 'rb') as f:
    posList = pickle.load(f)

width, height = 107, 48

def putTextRect(img, text, pos, scale = 3, thickness = 3, colorT = (255, 255, 255),
        colorR=(255,0,255), font = cv2.FONT_HERSHEY_PLAIN,
        offset=10, border=None, colorB = (0, 255, 0)):
        
    ox, oy = pos
    (w,h), _ = cv2.getTextSize(text, font, scale, thickness)
    x1, y1, x2, y2 = ox - offset, oy + offset, ox + w + offset, oy - h - offset
    cv2.rectangle(img, (x1, y1), (x2, y2), colorR, cv2.FILLED)
    if border is not None:
        cv2.rectangle(img, (x1, y1), (x2, y2), colorB, border)

    cv2.putText(img, text, (ox, oy), font, scale, colorT, thickness)

    return img, [x1, y2, x2, y1]

def carparkcheck(img):
    carparcount = 0
    for pos in posList:
        x,y = pos
        carpark_img = img[y:y+height, x:x+width]
        countwhite = cv2.countNonZero(carpark_img)

        if countwhite < 550:
            carparcount += 1
            color = (0,255,0)
        else:
            color = (0,0,255)

        thickness = 4;
        cv2.rectangle(frame, pos, (pos[0] + width, pos[1] + height), color, thickness)
        putTextRect(frame, str(countwhite), (x,y + height -3), scale = 1, thickness = 2, offset = 0, colorR = countwhite)

    putTextRect(frame, f'Free: {carparcount}/{len(posList)}', (100, 50), scale=3, thickness = 5, offset = 20, colorR = (0,200,0))


while True:
    ret, frame = cap.read()
    imgGray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray, (3,3), 1)
    imgThreshold = cv2.adaptiveThreshold(imgBlur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 25, 16)
    imgThreshold = cv2.medianBlur(imgThreshold, 5)

    carparkcheck(imgThreshold)

    if ret :
        cv2.imshow("Image", frame)
        # cv2.imshow("imgThreshold", imgThreshold)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

cv2.destroyAllWindows()