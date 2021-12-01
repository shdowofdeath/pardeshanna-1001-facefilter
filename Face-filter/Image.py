from const_libraries import *

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

    def integral_img(self):
        for i in range(ROWS):
            for j in range(COLS):
                z = self.arr[i - 1][j - 1] if (i > 0 and j > 0) else 0
                x = self.arr[i][j - 1] if j > 0 else 0
                y = self.arr[i - 1][j] if i > 0 else 0
                self.arr[i][j] = self.arr[i][j] + x + y - z