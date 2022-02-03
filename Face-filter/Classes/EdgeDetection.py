import cv2
from numpy import asarray
from Classes import Point

MINI_ROWS = 24
MINI_COLS = 24
MINI_GRID_SIDE = 1
NUM_OF_GRIDS = 24

def read_image(path):
    img = cv2.imread(path)
    return img

def resize_img(img, width, height):
    dim = (width, height)
    resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
    return resized

def greyscale(img):
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return imgGray


def img_to_array(img):
    pixels = asarray(img)
    pixels = pixels.astype('float32')
    pixels /= 255.0
    return pixels

def edge_check_horizontal(arr):
    for i in range(NUM_OF_GRIDS):
        for j in range(NUM_OF_GRIDS - 1):
            if (abs(arr[i][j] - arr[i][j + 1]) > 0.1):
                arr[i][j] = -1


def edge_check_vertical(arr):
    for i in range(NUM_OF_GRIDS - 1):
        for j in range(NUM_OF_GRIDS):
            if ((arr[i][j] != -1 or arr[i + 1][j] != -1) and (abs(arr[i][j] - arr[i + 1][j]) > 0.1)):
                arr[i][j] = -1


def draw_line(img, start_x, start_y, end_x, end_y, color):
    cv2.line(img, (start_x, start_y), (end_x, end_y), (255, color, 0), 1)
    return img


def draw_outline(start_coords, grid, img, marker, color):
    for i in range(NUM_OF_GRIDS):
        for j in range(NUM_OF_GRIDS):
            if (grid[i][j] == marker):
                img = draw_line(img, j + start_coords[1], i + start_coords[0], j + start_coords[1], i + start_coords[0],
                                color)
    return img


def edge_detection(pixels):
    start_row, end_row, start_col, end_col = 0, 1, 0, 1
    averages_grid = t = [[0] * MINI_ROWS for i in range(MINI_COLS)]
    counter = 1
    row_counter = 0
    col_counter = 0
    while start_row != MINI_ROWS:
        averages_grid[row_counter][col_counter] = pixels[start_row:end_row, start_col:end_col]
        counter = counter + 1
        if (end_col == MINI_COLS):
            start_row += 1
            end_row += 1
            start_col = 0
            end_col = 1
            row_counter = row_counter + 1
            col_counter = 0
        else:
            start_col += 1
            end_col += 1
            col_counter = col_counter + 1

    edge_check_horizontal(averages_grid)
    edge_check_vertical(averages_grid)
    return averages_grid

def print_img(img, averages_grid, start_coords):
    cv2.imshow("Before: ", img)
    img = draw_outline(start_coords, averages_grid, img, -1, 0)
    cv2.imshow("After: ", img)
    cv2.waitKey(0)
