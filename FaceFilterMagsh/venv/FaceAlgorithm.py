import cv2
import numpy as np
from numpy import asarray
from PIL import Image

ROWS = 368
COLS = 368
MINI_GRID_SIDE = 2
NUM_OF_GRIDS = ROWS//MINI_GRID_SIDE

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

def draw_line(img, start_x, start_y, end_x, end_y):
    cv2.line(img, (start_x, start_y), (end_x, end_y), (255, 0, 0), 3)
    return img

def draw_outline(grid, img):
    for i in range(NUM_OF_GRIDS):
        for j in range(NUM_OF_GRIDS):
            if(grid[i][j] == -1):
               img = draw_line(img, j * MINI_GRID_SIDE, i * MINI_GRID_SIDE, j *MINI_GRID_SIDE, i*MINI_GRID_SIDE)
    return img

def resize_img(img, width, height):
    dim = (width, height)
    resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
    return resized

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
    test_2 = read_image("../Resources/black_on_white.png")
    test_3 = read_image("../Resources/test_3.png")
    test_4 = read_image("../Resources/test_4.png")
    test_5 = read_image("../Resources/test_5.png")
    test_6 = read_image("../Resources/test_6.png")
    test_7 = read_image("../Resources/test_7.png")
    averages_grid, img = face_detection(test_1)
    cv2.imshow("Before: ", img)
    img = draw_outline(averages_grid, img)
    cv2.imshow("After: ", img)
    cv2.waitKey(0)
if __name__ == '__main__':
    main()
