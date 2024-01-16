import numpy as np
import cv2

circle = np.zeros((512, 512, 3), np.uint8) + 255
rectangle = np.zeros((512, 512, 3), np.uint8) + 255

cv2.circle(circle, (256, 256), 60, (255, 0, 0), -1)
cv2.rectangle(rectangle, (196, 196), (316, 316), (0, 0, 255), -1)

dst = cv2.addWeighted(circle, 0.8, rectangle, 0.2, 0)

cv2.imshow("circle", circle)
cv2.imshow("rectangle", rectangle)
cv2.imshow("dst", dst)

cv2.waitKey(0)
cv2.destroyAllWindows()