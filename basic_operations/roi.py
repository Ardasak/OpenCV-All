# roi --> region of interest

import cv2

img = cv2.imread("eomlions.jpg")
img1 = cv2.imread("eomlions.jpg")
img2 = img + img1
font = cv2.FONT_HERSHEY_DUPLEX

print(img.shape)

img[300:350, 1150:1250] = (255, 255, 255)
cv2.putText(img, "?", (1184, 344), font, 1.7, (0, 0, 0), 2)

cv2.imshow("image", img2)
cv2.imwrite("test.jpeg", img2)
cv2.waitKey(0)
cv2.destroyAllWindows()