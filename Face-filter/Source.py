from Image import *


def main():
    img = Image("Resources/test_1.png")
    img.greyscale()
    img.resize(ROWS, COLS)
    img.img_to_array()
    img.integral_img()
    cv2.imshow("After: ", img.data)
    cv2.waitKey(0)
if __name__ == '__main__':
    main()