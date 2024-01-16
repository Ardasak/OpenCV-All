import cv2

img = cv2.imread("images/helicopter.jpg", 0) # cv2.IMREAD_GRAYSCALE
img1 = cv2.imread("images/sudoku.jpg", 0)

ret, img_thresh = cv2.threshold(img1, 127, 255, cv2.THRESH_BINARY)

cv2.imshow("img", img1)
cv2.imshow("img thresh", img_thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()