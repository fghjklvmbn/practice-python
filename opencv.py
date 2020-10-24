import cv2

img = cv2.imread("test/kid.png")         #이미지 불러오기
img_grey = cv2.imread("test/kid.png", cv2.IMREAD_GRAYSCALE)

cv2.imshow("kid", img)
cv2.imshow("kid gray", img_grey)

cv2.waitKey(0)

cv2.imwrite("test/gray.png", img_grey)

