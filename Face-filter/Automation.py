import copy
from Classes.Image import *
from Classes.ClassifierCascade import *
from Parser.parser import load_stages
from Constants import const_nums
import time
import os

def automation():
    directory = 'FaceExamples/'
    success_list = []
    pics_list = []
    count = 0
    for filename in os.listdir(directory):
        if filename.endswith(".png")  and "test" in filename and  "bad" not in filename:
            pics_list.append(filename)
            #tic = time.perf_counter()
            print('FaceExamples/' + filename)
            img = Image('FaceExamples/' + filename)
            img.greyscale()
            img.resize(const_nums.ROWS, const_nums.COLS)
            img.img_to_array()
            #img.invert_img_array()
            img.integral_img()
            img.cache = copy.deepcopy(img.data)
            stages = load_stages()
            cascade = ClassifierCascade(stages)
            if(cascade.detect_face(img)):
                success_list.append(True)
            else:
                success_list.append(False)
            # cv2.imshow("GreyScale: ", img.data)
            # cv2.waitKey(0)
            # cv2.imshow("Real Final Image", img.whole_img)
            # cv2.waitKey(0)
    print(success_list)
    print(pics_list)
    print("Accuracy: " + str(success_list.count(True) / len(success_list)))

automation()