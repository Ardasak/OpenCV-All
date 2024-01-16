import numpy as np
import cv2 as cv
im = cv.imread('images/helicopter.jpg')
imgray = cv.cvtColor(im, cv.COLOR_BGR2GRAY)
ret, thresh = cv.threshold(imgray, 120, 255, 0)
contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)

cv.drawContours(imgray, contours, -1, (0,255,0), 3)

cv.imshow("im", imgray)
cv.imshow("thresh", thresh)
cv.waitKey(0)
cv.destroyAllWindows()