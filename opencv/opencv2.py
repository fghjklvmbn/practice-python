import cv2

img = cv2.imread("test/kid.png", 1)

cv2.imshow("park", img)
cv2.waitKey(0)

