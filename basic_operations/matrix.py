import cv2
import numpy as np

img = cv2.imread("eomlions.jpg")
row, col = img.shape[:2]

M = np.float32([[1, 0, 100], [0, 1, 100]])

dst = cv2.warpAffine(img, M, (row, col))
cv2.imshow("New", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()