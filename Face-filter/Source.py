import copy
from Classes.Image import *
from Classes.EdgeDetection import *
from Classes.ClassifierCascade import *
from Parser.parser import load_stages
from Constants import const_nums
import time

def main(data):
    #Calls Image Ctor
    # face_num = "1"
    # face_link = "FaceExamples/test_" + face_num + ".png"
    img = Image(data)
    #print(img.data)
    #sets image for edge detection
    test = data
    image = resize_img(test, const_nums.WIDTH, const_nums.LENGTH)
    imgGray = greyscale(image)
    pixels = img_to_array(imgGray)

    #sets image for face detection
    img.resize(const_nums.ROWS, const_nums.COLS)
    img.greyscale()
    img.img_to_array()
    img.integral_img()
    img.cache = copy.deepcopy(img.data)

    stages = load_stages()
    cascade = ClassifierCascade(stages)
    #Detect face
    is_face, avrg_coords = cascade.detect_face(img)

    if(is_face):
        averages_grid, avrg_coords = find_eye_coords(avrg_coords, pixels)
        return print_img(image, averages_grid, avrg_coords)
    else:
        print("Face was not found")

if __name__ == '__main__':
    main()