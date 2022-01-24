import cv2
import numpy as np
from numpy import asarray
from Constants import const_nums
import copy
"""
This is the Image class.

Contains the basic image function necessary for Image manipulation

Contains the Integral image feature which optimizes the algorithim
"""

class Image:
    def __init__(self, path):
        self.data = cv2.imread(path)#sets the image data from the path
        self.cache = 0
        self.whole_img = copy.deepcopy(self.data)
        #resize og image
        dim = (450, 450)
        self.whole_img = cv2.resize(self.data, dim, interpolation=cv2.INTER_AREA)
        self.size = self.data.shape
        self.path = path = path
        self.arr = [[]]

    def img_to_array(self):
        #this functions converts the image to a numpy array
        self.arr = asarray(self.data)
        self.arr = self.arr.astype('float32')
        self.arr /= 255.0
        self.invert_img_array()

    def invert_img_array(self):
        #makes black pixles 1
        #makes white pixles 0
        for row in range(const_nums.ROWS):
             for col in range(const_nums.COLS):
                invert_pixel = 1 - self.arr[row][col]
                self.arr[row][col] = invert_pixel


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
        for i in range(const_nums.ROWS):
            #goes through the columns
            for j in range(const_nums.COLS):
                #if row and column bigger than 0 (can use previous diagonal), save previous diagonal
                z = self.arr[i - 1][j - 1] if (i > 0 and j > 0) else 0
                #save previous column
                x = self.arr[i][j - 1] if j > 0 else 0
                #save previous row
                y = self.arr[i - 1][j] if i > 0 else 0
                self.arr[i][j] = self.arr[i][j] + x + y - z


    def draw_mini_grid(self, start, end):
        color = (255,0,255)
        thickness = 1
        cv2.rectangle(self.data, start, end, color, thickness)
        # cv2.imshow("GreyScale: ", self.data)
        # self.data = copy.deepcopy(self.cache)
        # cv2.waitKey(10)

    def draw_rects(self, rects, start_coords):
        start = (start_coords[0], start_coords[1])#start of mini grid
        end = (start_coords[0] + 24, start_coords[1] + 24)#end of mini grid
        self.draw_mini_grid(start, end)
        for rect in rects:
            if rect.weight < 0:#black feature
                color = (0,255,255)
            else:#white feature
                color = (255, 255, 0)
            thickness = -10
            start = (start_coords[0] + rect.x, start_coords[1] + rect.y)#start of feature
            end = (start_coords[0] + rect.x + rect.width, start_coords[1] + rect.y + rect.height)#end of feature
            cv2.rectangle(self.data, start, end, color, thickness)
        cv2.imshow("GreyScale: ", self.data)
        self.data = copy.deepcopy(self.cache)
        cv2.waitKey(1)

    # def print_stage_num(self, stage_num):
    #     org = (50, 50)
    #     font = cv2.FONT_HERSHEY_SIMPLEX
    #     color = (255,255,255)
    #     thickness = 2
    #     fontScale = 1
    #     self.data = copy.deepcopy(self.cache)
    #     cv2.putText(self.data, 'Stage: ' + str(stage_num), org, font, fontScale, color, thickness, cv2.LINE_AA)
    #     cv2.imshow("Stage num", self.data)
    #     self.data = copy.deepcopy(self.cache)
    #     cv2.waitKey(0)

    def print_og_image_face(self, x, y):
        x = int(x)
        y = int(y)
        dimensions = self.whole_img.shape
        height = self.whole_img.shape[0]
        width = self.whole_img.shape[1]
        area = height * width
        mini_height = const_nums.ROWS
        mini_width = const_nums.COLS
        mini_area = mini_height * mini_width

        relativity_x = int(width / mini_width)
        relativity_y = int(height / mini_height)
        x = x * relativity_x
        y = y * relativity_y

        width = 24 * relativity_x
        height = 24 * relativity_y

        start = (x, y)  # start of mini grid
        end = (x + width + 20, y + height + 20)  # end of mini grid
        color = (51, 255, 51)
        thickness = 1

        cv2.rectangle(self.whole_img, start, end, color, thickness)
        cv2.imshow("Real Image", self.whole_img)
        cv2.waitKey(0)
