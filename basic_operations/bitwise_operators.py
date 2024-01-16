import cv2
import numpy as np

img1 = cv2.imread("images\\bitwise_1.png")
img2 = cv2.imread("images\\bitwise_2.png")

bit_and = cv2.bitwise_and(img1, img2)
bit_or = cv2.bitwise_or(img1, img2)
bit_not = cv2.bitwise_not(img1)
bit_not2 = cv2.bitwise_not(img2)
bit_xor = cv2.bitwise_xor(img1, img2)

while True:
    cv2.imshow("Bitwise And", bit_and)
    cv2.imshow("Bitwise Or", bit_or)
    cv2.imshow("Bitwise Not", bit_not)
    cv2.imshow("Bitwise Not 2", bit_not2)
    cv2.imshow("Bitwise Xor", bit_xor)
    cv2.waitKey(0)
    cv2.destroyWindow("Bitwise And")
    break

