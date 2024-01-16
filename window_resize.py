import cv2

img = cv2.imread("eomlions.jpg")

cv2.namedWindow("EOMLions Linear", cv2.WINDOW_NORMAL)
cv2.namedWindow("EOMLions Area", cv2.WINDOW_NORMAL)

img1 = cv2.resize(img, (100, 100), interpolation=cv2.INTER_AREA)
img2 = cv2.resize(img, (100, 100), interpolation=cv2.INTER_LINEAR)

cv2.imshow("EOMLions Area", img1)
cv2.imshow("EOMLions Linear", img2)
cv2.waitKey(0)

cv2.destroyAllWindows()



