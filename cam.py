import cv2
import time
def time_snapshot():
    videoCaptureObject = cv2.VideoCapture(0)
    result = True
    while(result):
        ret,frame=videoCaptureObject.read()
        cv2.imwrite('Picture.jpg',frame)
        result = False
    videoCaptureObject.release()
    cv2.destroyAllWindows()
time_snapshot()