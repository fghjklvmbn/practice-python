import cv2

cap = cv2.VideoCapture("60fps .mp4")

while cap.isOpened():
    success, frame = cap.read()
    if success:
        cv2.imshow('camera window', frame)
        key = cv2.waitKey(0xFF)  #ESC 종료
        if (key == 27):
            break

cap.release()
cv2.destroyAllWindows()
