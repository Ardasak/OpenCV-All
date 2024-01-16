import cv2
import numpy as np

img = cv2.imread("eomlions.jpg")
row, col = img.shape[:2]

M = cv2.getRotationMatrix2D((col/2, row/2), 180, 1)

dst = cv2.warpAffine(img, M, (row, col))

cv2.imshow("dst", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()