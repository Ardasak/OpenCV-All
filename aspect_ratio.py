import cv2


def resizeWithAspectRatio(img, width = None, height = None, inter = cv2.INTER_AREA):
    (h,w) = img.shape[:2]

    if width is None and height is None:
        return img

    if width is None:
        r = height / h
        dimension = (int(w*r), height)
        print(dimension)

    else:
        r = width / w
        dimension = (width, int(h*r))
    
    return cv2.resize(img, dimension, interpolation = inter)

img = cv2.imread("images/eomlions.jpg")

img1 = resizeWithAspectRatio(img, height=200)


cv2.imshow("EOMLions", img)
cv2.imshow("EOMLionsResize", img1)


cv2.waitKey(0)
cv2.destroyAllWindows()