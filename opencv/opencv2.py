import numpy as np
import cv2

def showimage():
    imgfile = "images/과제.PNG"
    img = cv2.imread(imgfile, cv2.UNCHANGED)

    cv2.imshow('과제', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

showimage()
