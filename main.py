import cv2

cam = cv2.VideoCapture(0)

while cv2.waitKey(1) == -1:
    suc, frame = cam.read()
    if suc:
        cv2.imshow('Frame', frame)

cam.release()
cv2.destroyAllWindows()