import cv2

cap = cv2.VideoCapture(0)

codec = cv2.VideoWriter_fourcc("W", "M", "V", "2A")
frameRate = 20
resolution = (640, 480)
videoFileOutput = cv2.VideoWriter(
    "test.avi",
    codec,
    frameRate,
    resolution
)

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    videoFileOutput.write(frame)
    if ret:
        cv2.imshow("Webcam", frame)
    else:
        break

    if cv2.waitKey(30) == ord("q"):
        break

cap.release()
videoFileOutput.release()
cv2.destroyAllWindows()
