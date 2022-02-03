import copy

from Classes.Image import *
from Classes.EdgeDetection import *
from Classes.ClassifierCascade import *
from Parser.parser import load_stages
from Constants import const_nums
import time

def main():
    tic = time.perf_counter()
    img = Image("FaceExamples/test_17.png")

    #sets image for edge detection
    test = read_image("FaceExamples/test_17.png")
    image = resize_img(test, const_nums.ROWS, const_nums.COLS)
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
        averages_grid = edge_detection(pixels[avrg_coords[0]:(avrg_coords[0]+24), avrg_coords[1]:(avrg_coords[1]+24)])
        print_img(image, averages_grid, avrg_coords)


    #cv2.imshow("GreyScale: ", img.data)
    #cv2.waitKey(0)
    #cv2.imshow("Real Final Image", img.whole_img)
    #cv2.waitKey(0)

if __name__ == '__main__':
    main()