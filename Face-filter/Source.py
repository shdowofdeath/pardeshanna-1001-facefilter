from Classes.Image import *
from Classes.ClassifierCascade import *
from Parser.parser import load_stages


def main():
    img = Image("FaceExamples/test_1.png")
    img.greyscale()
    img.resize(ROWS, COLS)
    img.img_to_array()
    img.integral_img()
    stages = load_stages()
    cascade = ClassifierCascade(stages)
    cascade.detect_face(img)
    # cv2.imshow("GreyScale: ", img.data)
    # cv2.waitKey(0)

if __name__ == '__main__':
    main()