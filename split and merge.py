import cv2

cv2.namedWindow("EOMLions", cv2.WINDOW_NORMAL)
cv2.namedWindow("EOMLions Cropped", cv2.WINDOW_NORMAL)

img = cv2.imread("images/OpenCV.png")

b, g, r = cv2.split(img)

img1 = cv2.merge([r, r, r])

cv2.imshow("EOMLions", img)
cv2.imshow("B", b)
cv2.imshow("G", g)
cv2.imshow("R", r)
cv2.imshow("EOMLions Merged", img1)

cv2.waitKey(0)
cv2.destroyAllWindows()