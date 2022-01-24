import copy

from Classes.Image import *
from Classes.ClassifierCascade import *
from Parser.parser import load_stages
from Constants import const_nums
import time

def main():
    cap = cv2.VideoCapture(0)

    # run main loop
    # if we show one image after another, it becomes video
    stages = load_stages()
    while True:
        ret, frame = cap.read()  # read from camera
        img = Image(frame)
        img.greyscale()
        img.resize(const_nums.ROWS, const_nums.COLS)
        img.img_to_array()
        # img.invert_img_array()
        img.integral_img()
        img.cache = copy.deepcopy(img.data)
        cascade = ClassifierCascade(stages)
        cascade.detect_face(img)
        cv2.imshow('frame', img.whole_img)  # show image
        if cv2.waitKey(10) == ord('q'):  # wait a bit, and see keyboard press
            break  # if q pressed, quit

    # release things before quiting
    cap.release()
    cv2.destroyAllWindows()


    #cv2.imshow("GreyScale: ", img.data)
    #cv2.waitKey(0)
    #cv2.imshow("Real Final Image", img.whole_img)
    #cv2.waitKey(0)

if __name__ == '__main__':
    main()