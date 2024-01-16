import cv2

img = cv2.imread("eomlions.jpg", cv2.IMREAD_GRAYSCALE)

cv2.namedWindow("EOMLions", cv2.WINDOW_NORMAL)

cv2.imshow("EOMLions", img)
cv2.waitKey(5000)
cv2.destroyAllWindows()