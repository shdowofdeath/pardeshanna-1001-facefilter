import parser
from Classes.Image import *
from Constants.const_libraries import *

def main():
    img = Image("FaceExamples/test_1.png")
    img.greyscale()
    img.resize(ROWS, COLS)
    img.img_to_array()
    img.integral_img()

    stages = parser.load_stages()
    cascade = ClassifierCascade(stages)
    cascade.detect_face()

    cv2.imshow("GreyScale: ", img.data)
    cv2.waitKey(0)


if __name__ == '__main__':
    main()