from Classes.Filter import *

def main(data, image_file):
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
        facial_coords = find_eye_coords(avrg_coords, pixels)
        #img = print_img(image, averages_grid, avrg_coords)
        filters = filterCreator(image_file)
        filters[2].coords[0] = facial_coords[4][0]
        filters[2].coords[1] = facial_coords[4][1]
        filters[2].fixate()
        filters[2].paste_filter()

        return filters[2].image_after_filter
    else:
        print("Face was not found")

if __name__ == '__main__':
    main()