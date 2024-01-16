import cv2
import numpy as np

img = cv2.imread("eomlions.jpg")
dimension = img.shape
color = img[150, 200]

img[150:500, 200:250] = (255, 0, 0)
print(color)
print(dimension)

cv2.imshow("image",img)



if cv2.waitKey(0) == ord("q"):
    cv2.destroyAllWindows()