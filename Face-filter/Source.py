import cv2
import numpy as np
from numpy import asarray
from PIL import Image


ROWS = 400
COLS = 400

class Image:
    def __init__(self, path):
        self.data = cv2.imread(path)
        self.size = self.data.shape
        self.arr = [[]]

    def img_to_array(self):
        self.arr = asarray(self.data)
        self.arr = self.arr.astype('float32')
        self.arr /= 255.0

    def resize(self, width, height):
        dim = (width, height)
        self.data = cv2.resize(self.data, dim, interpolation=cv2.INTER_AREA)

    def greyscale(self):
        self.data = cv2.cvtColor(self.data, cv2.COLOR_BGR2GRAY)

    def get_img(self):
        return self.arr



def main():
    img = Image("./Resources/test.png")
    img.greyscale()
    img.img_to_array()
    img.resize(ROWS, COLS)
    print(img)

if __name__ == '__main__':
    main()