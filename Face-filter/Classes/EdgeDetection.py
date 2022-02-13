import cv2
from numpy import asarray
import numpy as np
from Classes import Point
from Constants import const_nums

# MINI_ROWS = 240
# MINI_COLS = 240
# MINI_GRID_SIDE = 1
# NUM_OF_GRIDS = 240

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
    for i in range(const_nums.FACE_LEN):
        for j in range(const_nums.FACE_LEN - 1):
            if (abs(arr[i][j] - arr[i][j + 1]) > const_nums.EDGES):
                arr[i][j] = -1


def edge_check_vertical(arr):
    for i in range(const_nums.FACE_LEN - 1):
        for j in range(const_nums.FACE_LEN):
            if ((arr[i][j] != -1 or arr[i + 1][j] != -1) and (abs(arr[i][j] - arr[i + 1][j]) > const_nums.EDGES)):
                arr[i][j] = -1


def draw_line(img, start_x, start_y, end_x, end_y, color):
    cv2.line(img, (start_x, start_y), (end_x, end_y), (255, color, 0), 1)
    return img


def draw_outline(start_coords, grid, img, marker, color):
    for i in range(const_nums.FACE_LEN):
        for j in range(const_nums.FACE_LEN):
            if (grid[i][j] == marker):
                img = draw_line(img, j + start_coords[1], i + start_coords[0], j + start_coords[1], i + start_coords[0],
                                color)
            if(grid[i][j] == -10):
                cv2.line(img, (j + start_coords[1], i + start_coords[0]), (j + start_coords[1], i + start_coords[0]), (0, 255, 128), 8)
    return img


def edge_detection(pixels):
    start_row, end_row, start_col, end_col = 0, 1, 0, 1
    averages_grid = np.empty([const_nums.FACE_LEN, const_nums.FACE_LEN])
    counter = 1
    row_counter = 0
    col_counter = 0
    while start_row != const_nums.FACE_LEN:
        averages_grid[row_counter][col_counter] = pixels[start_row:end_row, start_col:end_col]
        counter = counter + 1
        if (end_col == const_nums.FACE_LEN):
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
    #img = draw_outline(start_coords, averages_grid, img, -1, 0)
    cv2.rectangle(img, (start_coords[1], start_coords[0]), (start_coords[1] + const_nums.FACE_LEN, start_coords[0] + const_nums.FACE_LEN), (51, 255, 51), 1)
    return img
    #cv2.imshow("After: ", img)

def print_img_aut(img, averages_grid, start_coords):
    cv2.imshow("Before: ", img)
    img = draw_outline(start_coords, averages_grid, img, -1, 0)
    cv2.rectangle(img, (start_coords[1], start_coords[0]), (start_coords[1] + const_nums.FACE_LEN, start_coords[0] + const_nums.FACE_LEN), (51, 255, 51), 1)
    cv2.imshow("After: ", img)


def most_populated_index(arr, part):

    index = [0, 0, 0]
    for i in range(const_nums.MINI_FACE_LEN):
        for j in range(const_nums.MINI_FACE_LEN):
            if(arr[j][i] == -1):
                if(part == 1):#eyes
                    friends_in_rng = friends_in_range(j,i, arr)
                elif(part == 2):#mouth
                    friends_in_rng = friends_in_range_mouth(j, i, arr)

                if(friends_in_rng > index[2]):
                    index[1] = i
                    index[0] = j
                    index[2] = friends_in_rng
    return index


def friends_in_range(x,y,arr):
    counter = 0
    f_range = const_nums.RANGE
    if (x - f_range >= 0) and (y - f_range >= 0) and (x + f_range <= const_nums.MINI_FACE_LEN) and (y + f_range <= const_nums.MINI_FACE_LEN):
        checking_arr = arr[x-f_range:x+f_range, y-f_range:y+f_range]
        for i in range(f_range * 2):
            for j in range(f_range * 2):
                if(checking_arr[j][i] == -1):
                    counter = counter + 1
    return counter


def friends_in_range_mouth(x,y,arr):
    counter = 0
    vertical_range = const_nums.VERT_RANGE
    horizontal_range = const_nums.HORIZ_RANGE
    if (x - horizontal_range >= 0) and (y - vertical_range >= 0) and (x + horizontal_range <= const_nums.MINI_FACE_LEN) and (y + vertical_range <= const_nums.MINI_FACE_LEN):
        checking_arr = arr[x-horizontal_range:x+horizontal_range, y-vertical_range:y+vertical_range]
        for i in range(vertical_range * 2):
            for j in range(horizontal_range * 2):
                if(checking_arr[j][i] == -1):
                    counter = counter + 1
    #print("MOUTH")
    return counter


def print_face(self, x, y):
    x = int(x)
    y = int(y)
    dimensions = self.whole_img.shape
    height = self.whole_img.shape[0]
    width = self.whole_img.shape[1]
    area = height * width
    mini_height = 40
    mini_width = 40
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

def find_eye_coords(avrg_coords, pixels):
    avrg_coords[0] += 4
    avrg_coords[1] += 3
    avrg_coords[0] = avrg_coords[0] * const_nums.RELATIVITY
    avrg_coords[1] = avrg_coords[1] * const_nums.RELATIVITY
    averages_grid = edge_detection(pixels[avrg_coords[0]:(avrg_coords[0] + const_nums.FACE_LEN),
                                   avrg_coords[1]:(avrg_coords[1] + const_nums.FACE_LEN)])
    top_left = averages_grid[0:const_nums.MINI_FACE_LEN, 0:const_nums.MINI_FACE_LEN]
    top_right = averages_grid[0:const_nums.MINI_FACE_LEN, const_nums.MINI_FACE_LEN:const_nums.FACE_LEN]
    # bottom_left = averages_grid[120:240, 0:120]
    # bottom_right = averages_grid[120:240, 120:240]

    bottom = averages_grid[const_nums.MINI_FACE_LEN:const_nums.FACE_LEN, 0:const_nums.FACE_LEN]

    top_left_index = most_populated_index(top_left, 1)
    top_right_index = most_populated_index(top_right, 1)
    bottom_index = most_populated_index(bottom, 2)

    averages_grid[top_left_index[0]][top_left_index[1]] = -10
    averages_grid[top_right_index[0]][top_right_index[1] + const_nums.MINI_FACE_LEN] = -10
    averages_grid[bottom_index[0] + const_nums.MINI_FACE_LEN][bottom_index[1]] = -10
    # averages_grid[bottom_right_index[0] + 120][bottom_right_index[1] + 120] = -10

    return averages_grid, avrg_coords
