# initialize the camera
from cv2 import *

cam = VideoCapture(2)   # 0 -> index of camera
s, img = cam.read()
if s:    # frame captured without any errors
    imwrite("filename.jpg", img)  # save image
