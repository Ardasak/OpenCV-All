import cv2
import numpy as np

canvas = np.zeros((512, 512, 3), dtype=np.uint8) + 255

font1 = cv2.FONT_HERSHEY_COMPLEX

cv2.line(canvas, (50, 50), (350,200), color=(255, 0, 0), thickness=3)

cv2.rectangle(canvas, (50, 50), ( 350, 200), color=(0, 0, 255), thickness=3)
cv2.circle(canvas, (450,450), 45, color=(0, 255, 0), thickness=-1)

# cv2.line(canvas, (150, 400), (200,450), color=(0, 0, 255), thickness=2)
# cv2.line(canvas, (200, 450), (150,500), color=(0, 0, 255), thickness=2)
# cv2.line(canvas, (150, 500), (150,400), color=(0, 0, 255), thickness=2)

points = np.array([[[150, 400], [200, 450], [150, 500]]], np.int32)

cv2.polylines(canvas, points, isClosed=True, color=(0, 255, 0), thickness=2)
cv2.ellipse(canvas, (300, 450), (50,30), 45, 180, 360, (255, 0, 0), 3)
# cv2.polylines(canvas, [cv2.ellipse2Poly((300, 450), (50, 30), 45, 0, 360, 5)], isClosed=True, color=(0, 255, 0), thickness=2)

cv2.putText(canvas, "deryam", (300,450), font1, fontScale=1, color=(255, 0, 0), thickness=2)

cv2.imshow("Canvas", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()