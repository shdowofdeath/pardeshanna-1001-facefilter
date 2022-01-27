import cv2
import numpy as np
from numpy import asarray
from PIL import Image

ROWS = 368
COLS = 368
MINI_GRID_SIDE = 1
NUM_OF_GRIDS = ROWS//MINI_GRID_SIDE


class Point:
    def __init__(self, x, y, max):
        self.x = x
        self.y = y
        self.max = max
    def set_x(self, x):
        self.x =  x
    def set_y(self, y):
        self.y =  y
    def get_x(self):
        return self.x
    def get_y(self):
        return self.y
    def get_max(self):
        return self.max
    def set_max(self, max):
        self.max =  max
def read_image(path):
    img = cv2.imread(path)
    return img

def get_image_size(img):
    rows, cols = img.shape
    return rows, cols

def greyscale(img):
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return imgGray

def img_to_array(img):
    pixels = asarray(img)
    pixels = pixels.astype('float32')
    pixels /= 255.0
    return pixels

def grid_array(start_row, end_row, start_col, end_col, arr):
    grid = arr[start_row:end_row, start_col:end_col]
    return grid

def get_grid_avg(grid, rows, cols):
    avg = 0
    for i in range(rows):
        for j in range(cols):
            avg = avg + grid[i][j]
    avg = avg / (rows*cols)
    return avg

def create_averages_grid(arr):
    grid = arr[0:(NUM_OF_GRIDS + 1), 0:(NUM_OF_GRIDS + 1)]
    return grid

def init_avg_arr(averages_grid):
    i = 0
    j = 0
    for i in range(NUM_OF_GRIDS):
        for j in range(NUM_OF_GRIDS):
            if (averages_grid[i][j] >= 0.3):
                averages_grid[i][j] = 1
            else:
                averages_grid[i][j] = 0
            
def edge_check_horizontal(arr):
    for i in range(NUM_OF_GRIDS):
        for j in range(NUM_OF_GRIDS - 1):
            if(abs(arr[i][j] - arr[i][j+1]) > 0.1):
                arr[i][j] = -1

def edge_check_vertical(arr):
    for i in range(NUM_OF_GRIDS - 1):
        for j in range(NUM_OF_GRIDS):
            if((arr[i][j] != -1 or arr[i+1][j] != -1) and (abs(arr[i][j] - arr[i+1][j]) > 0.1)):
                arr[i][j] = -1

def draw_line(img, start_x, start_y, end_x, end_y, color):
    cv2.line(img, (start_x, start_y), (end_x, end_y), (255, color, 0), 1)
    return img

def draw_outline(grid, img, marker, color):
    for i in range(NUM_OF_GRIDS):
        for j in range(NUM_OF_GRIDS):
            if(grid[i][j] == marker):
               img = draw_line(img, j * MINI_GRID_SIDE, i * MINI_GRID_SIDE, j *MINI_GRID_SIDE, i*MINI_GRID_SIDE, color)
    return img

def resize_img(img, width, height):
    dim = (width, height)
    resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
    return resized


def find_extreme_case_points(averages_grid):
    highest = Point(NUM_OF_GRIDS - 1, NUM_OF_GRIDS -1, 0)
    lowest = Point(0, 0, 0)
    left = Point(NUM_OF_GRIDS -1, NUM_OF_GRIDS -1, 0)
    right = Point(0, 0, 0)
    for i in range(NUM_OF_GRIDS):
        for j in range(NUM_OF_GRIDS):
            if(averages_grid[i][j] == -1):
                if(i < highest.get_y()):
                    highest.set_x(j)
                    highest.set_y(i)
                if(i > lowest.get_y()):
                    lowest.set_x(j)
                    lowest.set_y(i)
                if(j > right.get_x()):
                    right.set_x(j)
                    right.set_y(i)
                if(j < left.get_x()):
                    left.set_x(j)
                    left.set_y(i)
    return highest, lowest, left, right

    return averages_grid

def get_rectangle_coordinates(highest, lowest, left, right, average_grid):

    left_top_point = Point(left.get_x(), highest.get_y(), 0)
    right_top_point = Point(right.get_x(), highest.get_y(), 0)
    left_bottom_point = Point(left.get_x(), lowest.get_y(), 0)
    right_bottom_point = Point(right.get_x(), lowest.get_y(), 0)
    return left_top_point, right_top_point, left_bottom_point, right_bottom_point

def draw_rectangle(left_top_point, right_bottom_point, img):
    cv2.rectangle(img,(left_top_point.get_x(),left_top_point.get_y()),(right_bottom_point.get_x(),right_bottom_point.get_y()),(0,255,0),2)
    return img

def draw_line_2(img, start_point, end_point):
    cv2.line(img, (start_point.get_x(), start_point.get_y()), (end_point.get_x(), end_point.get_y()), (255, 255, 200), 2)
    return img
def occ_arr_counter(arr, rows, cols):
    counter = 0
    for i in range(rows):
        for j in range(cols):
            if(arr[i][j] == -1):
               counter = counter + 1
    return counter

def get_mid_point(arr):
    max_point = Point(0,0,0)
    max = 0
    for i in range(NUM_OF_GRIDS):
        for j in range(NUM_OF_GRIDS):
            if(i - 170 >= 0 and j - 105 >= 0 and i + 170 <= 368  and j + 105 <= 368):
                array_to_check = grid_array(i - 170, i + 170 , j - 105, j + 105, arr)
                rows = len(array_to_check)
                cols = len(array_to_check[0])
                max = occ_arr_counter(array_to_check, rows, cols)
                if(max_point.get_max() < max):
                    max_point.set_max(max)
                    max_point.set_x(i)
                    max_point.set_y(j)
    return max_point

def face_detection(img):
    img_black = read_image("../Resources/black.png")
    start_row, end_row, start_col, end_col = 0, MINI_GRID_SIDE, 0, MINI_GRID_SIDE
    img = resize_img(img, ROWS, COLS)
    imgGray = greyscale(img)
    imgBlack = greyscale(img_black)
    rows, cols = get_image_size(imgGray)
    pixels = img_to_array(imgGray)
    black_pixels = img_to_array(imgBlack)
    averages_grid = create_averages_grid(black_pixels)
    counter = 1
    row_counter = 0
    col_counter = 0
    while start_row != ROWS:

        grid = grid_array(start_row, end_row, start_col, end_col, pixels)
        grid_avg = get_grid_avg(grid, MINI_GRID_SIDE, MINI_GRID_SIDE)
        averages_grid[row_counter][col_counter] = grid_avg
        counter = counter + 1
        if (end_col == cols):
            start_row += MINI_GRID_SIDE
            end_row += MINI_GRID_SIDE
            start_col = 0
            end_col = MINI_GRID_SIDE
            row_counter = row_counter + 1
            col_counter = 0
        else:
            start_col += MINI_GRID_SIDE
            end_col += MINI_GRID_SIDE
            col_counter = col_counter + 1
    # init_avg_arr(averages_grid)
    edge_check_horizontal(averages_grid)
    edge_check_vertical(averages_grid)
    return averages_grid, img

def main():


    test_1 = read_image("../Resources/lena.png")
    # test_2 = read_image("../Resources/black_on_white.png")
    # test_3 = read_image("../Resources/test_3.png")
    # test_4 = read_image("../Resources/test_4.png")
    # test_5 = read_image("../Resources/test_5.png")
    # test_6 = read_image("../Resources/test_6.png")
    # test_7 = read_image("../Resources/test_7.png")
    # test_8 = read_image("../Resources/test_8.png")
    # test_9 = read_image("../Resources/test_9.png")
    # test_10 = read_image("../Resources/test_10.png")
    # test_11 = read_image("../Resources/test_11.png")
    test_12 = read_image("../Resources/test_12.png")
    averages_grid, img = face_detection(test_12)
    highest, lowest, left, right = find_extreme_case_points(averages_grid)
    #mid_point = get_mid_point(averages_grid)
    left_top_point, right_top_point, left_bottom_point, right_bottom_point = get_rectangle_coordinates(highest, lowest, left, right, averages_grid)
    cv2.imshow("Before: ", img)
    img = draw_rectangle(left_top_point, right_bottom_point, img)
    left_rect = Point(left_top_point.get_x(), abs(left_bottom_point.get_y() + left_top_point.get_y()) // 2, 0)
    right_rect = Point(right_top_point.get_x(), abs(right_bottom_point.get_y() + right_top_point.get_y()) // 2, 0)
    top_rect = Point(abs(left_top_point.get_x() + right_top_point.get_x()) // 2, right_top_point.get_y(), 0)
    bottom_rect = Point(abs(left_top_point.get_x() + right_top_point.get_x()) // 2, left_bottom_point.get_y(), 0)
    img = draw_line_2(img, left_rect, right_rect)
    img = draw_line_2(img, top_rect, bottom_rect)
    img = draw_outline(averages_grid, img, -1, 0)
    cv2.imshow("After: ", img)
    cv2.waitKey(0)
if __name__ == '__main__':
    main()
