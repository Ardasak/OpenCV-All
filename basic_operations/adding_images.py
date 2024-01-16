import numpy as np
import cv2

circle = np.zeros((512, 512, 3), np.uint8)
rectangle = np.zeros((512, 512, 3), np.uint8)


cv2.circle(circle, (256, 256), 60, (255, 0, 0), -1)
cv2.rectangle(rectangle, (196, 196), (316, 316), (0, 0, 255), -1)

rectangleAndCircle = circle + rectangle # or preferably cv2.add(circle, rectangle)

cv2.namedWindow("circle", cv2.WINDOW_NORMAL)
cv2.namedWindow("rectangle", cv2.WINDOW_NORMAL)
cv2.namedWindow("together", cv2.WINDOW_NORMAL)

cv2.imshow("circle", circle)
cv2.imshow("rectangle", rectangle)
cv2.imshow("together", rectangleAndCircle)

cv2.waitKey(0)
cv2.destroyAllWindows()