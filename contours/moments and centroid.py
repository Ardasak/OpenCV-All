import cv2

img = cv2.imread("images/contour.png")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_,thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

contours,hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# cnt = contours[0]
# M = cv2.moments(cnt)

# X = int(M["m10"]/M['m00'])
# Y = int(M['m01']/M['m00'])

# cv2.circle(img, (X, Y), 3, (255, 255, 255), 3)
cv2.drawContours(img, contours, -1, (0, 0, 255), 3)

cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()