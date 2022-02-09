import copy

from Classes.Image import *
from Classes.EdgeDetection import *
from Classes.ClassifierCascade import *
from Parser.parser import load_stages
from Constants import const_nums
import time

def main():
    tic = time.perf_counter()
    face_num = "1"
    face_link = "FaceExamples/test_" + face_num + ".png"
    img = Image(face_link)

    #sets image for edge detection
    test = read_image(face_link)
    image = resize_img(test, 400, 400)
    imgGray = greyscale(image)
    pixels = img_to_array(imgGray)

    #sets image for face detection
    img.resize(const_nums.ROWS, const_nums.COLS)
    img.greyscale()
    img.img_to_array()
    #img.invert_img_array()
    img.integral_img()
    img.cache = copy.deepcopy(img.data)
    stages = load_stages()
    cascade = ClassifierCascade(stages)
    is_face, avrg_coords = cascade.detect_face(img)

    if(is_face):
        avrg_coords[0] = avrg_coords[0] * 10
        avrg_coords[1] = avrg_coords[1] * 10
        averages_grid = edge_detection(pixels[avrg_coords[0]:(avrg_coords[0]+240), avrg_coords[1]:(avrg_coords[1]+240)])
        top_left = averages_grid[0:120, 0:120]
        top_right = averages_grid[0:120, 120:240]
        # bottom_left = averages_grid[120:240, 0:120]
        # bottom_right = averages_grid[120:240, 120:240]

        top_left_index = most_populated_index(top_left)
        top_right_index = most_populated_index(top_right)
        # bottom_left_index = most_populated_index(bottom_left)
        # bottom_right_index = most_populated_index(bottom_right)

        averages_grid[top_left_index[0]][top_left_index[1]] = -10
        averages_grid[top_right_index[0]][top_right_index[1] + 120] = -10
        #averages_grid[bottom_left_index[0] + 120][bottom_left_index[1]] = -10
        #averages_grid[bottom_right_index[0] + 120][bottom_right_index[1] + 120] = -10
        print_img(image, averages_grid, avrg_coords)
        cv2.waitKey(0)
    #cv2.imshow("Real Final Image", img.whole_img)
    #cv2.waitKey(0)

if __name__ == '__main__':
    main()