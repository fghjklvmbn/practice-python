import numpy as np
import cv2

imgfile = "images/과제.PNG"
img = cv2.imread(imgfile, cv2.RGBT2GREY)

cv2.imshow('과제', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

showimage()
