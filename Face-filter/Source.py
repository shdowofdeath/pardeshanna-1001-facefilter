from Classes.Filter import *
from Classes.EdgeDetection import *

def add_filter(image, filters,facial_coords, index, is_add_filter):
    filters[index].img = image

    filters[index].coords[0] = facial_coords[index+2][0]
    filters[index].coords[1] = facial_coords[index+2][1]
    filters[index].fixate()
    if (is_add_filter):
        filters[index].paste_filter()
    else:
        filters[index].image_after_filter = image

    return filters[index].image_after_filter


def run(data, image_file, filters_arr, choice):

    #Calls Image Ctor
    img = Image(data)

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

    stages = load_stages()#loads stages from xml
    cascade = ClassifierCascade(stages)
    #Detect face
    is_face, avrg_coords = cascade.detect_face(img)

    if(is_face):#if face was found

        if(choice == 0):#edge detection
            averages_grid = find_eye_coords(avrg_coords, pixels, 0)
            final_img = print_img_aut(image, averages_grid, avrg_coords)
            return final_img

        elif(choice == 1):#filters
            facial_coords = find_eye_coords(avrg_coords, pixels, 1)

            filters = filterCreator(image_file)

            filters[0].image_after_filter = add_filter(image_file, filters, facial_coords, 0, filters_arr[0])#glasses
            filters[1].image_after_filter = add_filter(filters[0].image_after_filter, filters, facial_coords, 1, filters_arr[1])#lips
            filters[2].image_after_filter = add_filter(filters[1].image_after_filter, filters, facial_coords, 2, filters_arr[2])#hat

            return filters[2].image_after_filter

    else:
        print("Face was not found")