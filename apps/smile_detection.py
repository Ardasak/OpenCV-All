import numpy as np
import cv2

cap = cv2.VideoCapture(0)

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_smile.xml')

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (255, 0, 0), 5)
        roi_gray = gray[int(y + h/2):y+h, x: x+w]
        roi_color = frame[int(y + h/2):y+h, x: x+w]
        smiles = smile_cascade.detectMultiScale(roi_gray, 1.1, 15)
        for (sx, sy, sw, sh) in smiles:
            cv2.rectangle(roi_color, (sx, sy), (sx + sw, sy + sh), (0, 255, 0), 5)



    cv2.imshow("frame", frame)

    if(cv2.waitKey(1) == ord("q")):
        break

cap.release()
cv2.destroyAllWindows()