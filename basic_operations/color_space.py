import cv2

img = cv2.imread("eomlions.jpg")
img1 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow("Image", img)
cv2.imwrite("cizim/haha.jpg", img1)

cv2.waitKey(0)
cv2.destroyAllWindows()