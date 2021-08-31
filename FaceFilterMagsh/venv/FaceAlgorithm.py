import cv2
import numpy as np
from numpy import asarray
'''
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)'''
img = cv2.imread("../Resources/lena.png")

while True:
    #success, img = cap.read()
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Video", imgGray)
    rows, cols = imgGray.shape
    pixels = asarray(imgGray)
    pixels = pixels.astype('float32')
    pixels /= 255.0
    rows, cols = imgGray.shape

    print(pixels)
    print("DONE")
    if cv2.waitKey(1) & 0XFF == ord('q'):
        break