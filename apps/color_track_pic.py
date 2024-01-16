import cv2
import numpy as np

bgr_img = cv2.imread("images/colors.png")
hsv_img = cv2.cvtColor(bgr_img, cv2.COLOR_BGR2HSV)

def red_hsv():
    lower_hsv_1 = np.array([0, 175, 20])
    upper_hsv_1 = np.array([10, 255, 255])

    lower_hsv_2 = np.array([170, 175, 20])
    upper_hsv_2 = np.array([180, 255, 255])

    mask1 = cv2.inRange(hsv_img, lower_hsv_1, upper_hsv_1)
    mask2 = cv2.inRange(hsv_img, lower_hsv_2, upper_hsv_2)

    return mask1 + mask2

def green_hsv():
    # lower_hsv = np.array([40, 150, 20])
    # upper_hsv = np.array([70, 255, 255])

    lower_hsv = np.array([110,50,50])
    upper_hsv = np.array([130,255,255])

    mask = cv2.inRange(hsv_img, lower_hsv, upper_hsv)
    return mask

mask = red_hsv() + green_hsv()

detected_img = cv2.bitwise_and(bgr_img,bgr_img, mask=mask)

cv2.imshow("original", bgr_img)
cv2.imshow("img", detected_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
