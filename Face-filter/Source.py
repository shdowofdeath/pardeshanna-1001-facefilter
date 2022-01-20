import copy

from Classes.Image import *
from Classes.ClassifierCascade import *
from Parser.parser import load_stages
from Constants import const_nums
import time

def main():
    tic = time.perf_counter()
    img = Image("FaceExamples/test_18.png")
    img.greyscale()
    img.resize(const_nums.ROWS, const_nums.COLS)
    img.img_to_array()
    #img.invert_img_array()
    img.integral_img()
    img.cache = copy.deepcopy(img.data)
    stages = load_stages()
    cascade = ClassifierCascade(stages)
    cascade.detect_face(img)
    # cv2.imshow("GreyScale: ", img.data)
    # cv2.waitKey(0)
    cv2.imshow("Real Final Image", img.whole_img)
    cv2.waitKey(0)

if __name__ == '__main__':
    main()