from Constants.const_libraries import *

"""
This is the Image class.

Contains the basic image function necessary for Image manipulation

Contains the Integral image feature which optimizes the algorithim
"""

class Image:
    def __init__(self, path):
        self.data = cv2.imread(path)#sets the image data from the path
        self.size = self.data.shape
        self.arr = [[]]

    def img_to_array(self):
        #this functions converts the image to a numpy array
        self.arr = asarray(self.data)
        self.arr = self.arr.astype('float32')
        self.arr /= 255.0

    def resize(self, width, height):
        #this function resizes the image
        dim = (width, height)
        self.data = cv2.resize(self.data, dim, interpolation=cv2.INTER_AREA)

    def greyscale(self):
        #this function converts the image to greyscale
        self.data = cv2.cvtColor(self.data, cv2.COLOR_BGR2GRAY)

    def get_img(self):
        return self.arr

    def integral_img(self):
        #goes through the rows
        for i in range(ROWS):
            #goes through the columns
            for j in range(COLS):
                #if row and column bigger than 0 (can use previous diagonal), save previous diagonal
                z = self.arr[i - 1][j - 1] if (i > 0 and j > 0) else 0
                #save previous column
                x = self.arr[i][j - 1] if j > 0 else 0
                #save previous row
                y = self.arr[i - 1][j] if i > 0 else 0
                self.arr[i][j] = self.arr[i][j] + x + y - z