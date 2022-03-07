import cv2
from numpy import asarray
import numpy as np
from Constants import const_nums

# MINI_ROWS = 240
# MINI_COLS = 240
# MINI_GRID_SIDE = 1
# NUM_OF_GRIDS = 240

def read_image(path):
    #reads image from path
    img = cv2.imread(path)
    return img

def resize_img(img, width, height):
    #resizes image
    dim = (width, height)
    resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
    return resized

def greyscale(img):
    #converts the image to greyscale
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return imgGray


def img_to_array(img):
    #converts the image to an array of values from 0 to 1
    pixels = asarray(img)
    pixels = pixels.astype('float32')
    pixels /= 255.0
    return pixels

def edge_check_horizontal(arr):
    #checks if there are edges between horizontal pixels
    for i in range(const_nums.FACE_LEN):
        for j in range(const_nums.FACE_LEN - 1):
            if (abs(arr[i][j] - arr[i][j + 1]) > const_nums.EDGES):#checks if there is an edge based on the condition
                arr[i][j] = -1#marks the index


def edge_check_vertical(arr):
    # checks if there are edges between vertical pixels
    for i in range(const_nums.FACE_LEN - 1):
        for j in range(const_nums.FACE_LEN):
            if ((arr[i][j] != -1 or arr[i + 1][j] != -1) and (abs(arr[i][j] - arr[i + 1][j]) > const_nums.EDGES)):#checks if there is an edge based on the condition
                arr[i][j] = -1#marks the index


def draw_line(img, start_x, start_y, end_x, end_y, color):
    #this function draws a line on the image
    cv2.line(img, (start_x, start_y), (end_x, end_y), (255, color, 0), 1)
    return img


def draw_outline(start_coords, grid, img, marker, color):
    #this function outlines the edges that were detected in the image and marks the mouth and eyes
    for i in range(const_nums.FACE_LEN):
        for j in range(const_nums.FACE_LEN):
            if (grid[i][j] == marker):#the index is marked as an edge
                 img = draw_line(img, j + start_coords[1], i + start_coords[0], j + start_coords[1], i + start_coords[0], color)
            if(grid[i][j] == -10):#the index is marked as an eye or mouth
                cv2.line(img, (j + start_coords[1], i + start_coords[0]), (j + start_coords[1], i + start_coords[0]), (0, 255, 128), 10)
    return img


def edge_detection(pixels):
    '''
    This function checks where the edges of an image are and returns a marked array with edges
    '''
    averages_grid = np.empty([const_nums.FACE_LEN, const_nums.FACE_LEN])#initializes return list
    averages_grid = np.copy(pixels)#copies pixels to averages_grid
    edge_check_horizontal(averages_grid)
    edge_check_vertical(averages_grid)
    return averages_grid

def print_img_aut(img, averages_grid, start_coords):
    #This is a function for the Automation that prints out the image
    img = draw_outline(start_coords, averages_grid, img, -1, 0)
    cv2.rectangle(img, (start_coords[1], start_coords[0]), (start_coords[1] + const_nums.FACE_LEN, start_coords[0] + const_nums.FACE_LEN), (51, 255, 51), 1)
    return img

def most_populated_index(arr, part):
    '''
    This function finds the most populated index in the face
    in order to find where the eyes mouth and nose are
    :param arr: the array of the face
    :param part: the part of the face
    :return:
    '''
    index = [0, 0, 0]
    for i in range(const_nums.MINI_FACE_LEN):
        for j in range(const_nums.MINI_FACE_LEN):
            if(arr[j][i] == -1):#if the index is marked
                if(part == 1):#eyes
                    friends_in_rng = pixels_in_range(j,i, arr)
                elif(part == 2):#mouth
                    friends_in_rng = pixels_in_range_mouth(j, i, arr)

                if(friends_in_rng > index[2]):#If the index is more populated
                    index[1] = i
                    index[0] = j
                    index[2] = friends_in_rng
    return index


def pixels_in_range(x,y,arr):
    counter = 0
    f_range = const_nums.RANGE#the range to search for marked indexes
    if (x - f_range >= 0) and (y - f_range >= 0) and (x + f_range <= const_nums.MINI_FACE_LEN) and (y + f_range <= const_nums.MINI_FACE_LEN):#checks the validity of the index
        checking_arr = arr[x-f_range:x+f_range, y-f_range:y+f_range]#return a slice array in the range each direction from the current pixel
        for i in range(f_range * 2):
            for j in range(f_range * 2):
                if(checking_arr[j][i] == -1):#counts number of marked pixels
                    counter = counter + 1
    return counter


def pixels_in_range_mouth(x,y,arr):
    counter = 0
    vertical_range = const_nums.VERT_RANGE#the range to search for marked indexes vertically
    horizontal_range = const_nums.HORIZ_RANGE#the range to search for marked indexes horizontaly
    if (x - horizontal_range >= 0) and (y - vertical_range >= 0) and (x + horizontal_range <= const_nums.MINI_FACE_LEN) and (y + vertical_range <= const_nums.MINI_FACE_LEN):#checks the validity of the index
        checking_arr = arr[x-horizontal_range:x+horizontal_range, y-vertical_range:y+vertical_range]#return a slice array in the range each direction from the current pixel
        for i in range(vertical_range * 2):
            for j in range(horizontal_range * 2):
                if(checking_arr[j][i] == -1):#counts number of marked pixels
                    counter = counter + 1
    return counter


def fixate_coords(coords):
    coords[0] += 4
    coords[1] += 3
    coords[0] = coords[0] * const_nums.RELATIVITY
    coords[1] = coords[1] * const_nums.RELATIVITY
    return coords

def slice_array(array):
    top_left = array[0:const_nums.MINI_FACE_LEN,
               0:const_nums.MINI_FACE_LEN]  # slices the top left part of the face
    top_right = array[0:const_nums.MINI_FACE_LEN,
                const_nums.MINI_FACE_LEN:const_nums.FACE_LEN]  # slices the top right part of the face
    bottom = array[const_nums.MINI_FACE_LEN:const_nums.FACE_LEN,
             0:const_nums.FACE_LEN]  # slices the bottom part of the face
    return top_left, top_right, bottom

def mark_facial_features(arr, left, right, bottom):
    #This function marks the indexes of the main features of the face
    arr[left[0]][left[1]] = -10  # left eye
    arr[right[0]][right[1] + const_nums.MINI_FACE_LEN] = -10  # right eye
    arr[bottom[0] + const_nums.MINI_FACE_LEN][bottom[1]] = -10  # mouth
    return arr

def create_filter_coords(left, right, bottom, avrg_coords):
    #This function creates a list of the coords where the filters should be placed
    facial_coords = []
    facial_coords.append((left[1] + avrg_coords[1], left[0] + avrg_coords[0]))#Left eye
    facial_coords.append((right[1] + avrg_coords[1] + const_nums.MINI_FACE_LEN, right[0] + avrg_coords[0]))#Right eye
    facial_coords.append(((facial_coords[0][0] + facial_coords[1][0]) // 2, (facial_coords[0][1] + facial_coords[1][1]) // 2))#Middle of eyes
    facial_coords.append((bottom[1] + avrg_coords[1], bottom[0] + avrg_coords[0] + const_nums.MINI_FACE_LEN))#Mouth
    facial_coords.append((avrg_coords[1] + 100, avrg_coords[0]))#Head

    return facial_coords
def find_eye_coords(avrg_coords, pixels, choice):
    facial_coords = []
    avrg_coords = fixate_coords(avrg_coords)

    averages_grid = edge_detection(pixels[avrg_coords[0]:(avrg_coords[0] + const_nums.FACE_LEN), avrg_coords[1]:(avrg_coords[1] + const_nums.FACE_LEN)])#returns the marked array of the face

    top_left, top_right, bottom = slice_array(averages_grid)

    top_left_index = most_populated_index(top_left, 1)#Finds left eye coords
    top_right_index = most_populated_index(top_right, 1)#Finds right eye coords
    bottom_index = most_populated_index(bottom, 2)#finds mouth coords

    if(choice == 0):#edge detection
        averages_grid = mark_facial_features(averages_grid, top_left_index, top_right_index, bottom_index)
        return averages_grid

    if(choice == 1):#filters
        facial_coords = create_filter_coords(top_left_index, top_right_index, bottom_index, avrg_coords)
        return facial_coords
