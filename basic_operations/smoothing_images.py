import cv2
import numpy as np

img_filter = cv2.imread("images\\filter.png")
img_bilateral = cv2.imread("images\\bilateral.png")
img_median = cv2.imread("images\\median.png")

blur = cv2.blur(img_filter, (5, 5))
blur_g = cv2.GaussianBlur(img_filter, (5,5), cv2.BORDER_DEFAULT)

blur_m = cv2.medianBlur(img_median, 9)

blur_b = cv2.bilateralFilter(img_bilateral, 3, 90, 10)
# cv2.imshow("original", img_filter)
# cv2.imshow("blur_filter", blur)
# cv2.imshow("blur_gaussian", blur_g)

# cv2.imshow("original", img_median)
# cv2.imshow("blur_median", blur_m)

cv2.imshow("test", img_bilateral)
cv2.imshow("Bilateral blur", blur_b)

cv2.waitKey(0)
cv2.destroyAllWindows()