from Classes.Filter import *

def add_filter(image, filters,facial_coords, index, is_add_filter):
    filters[index].img = image

    filters[index].coords[0] = facial_coords[index+2][0]
    filters[index].coords[1] = facial_coords[index+2][1]
    filters[index].fixate()
    if (is_add_filter):
        filters[index].paste_filter()

    return filters[index].image_after_filter


def main(data, image_file, filters_arr):

    print(filters_arr)

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
        facial_coords = find_eye_coords(avrg_coords, pixels)
        #img = print_img(image, averages_grid, avrg_coords)

        filters = filterCreator(image_file)

        filters[0].image_after_filter = add_filter(image_file, filters, facial_coords, 0, filters_arr[0])#glasses
        filters[1].image_after_filter = add_filter(filters[0].image_after_filter, filters, facial_coords, 1, filters_arr[1])#lips
        filters[2].image_after_filter = add_filter(filters[1].image_after_filter, filters, facial_coords, 2, filters_arr[2])#hat

        """
        if(filters_arr[0]):
            filters[2].coords[0] = facial_coords[4][0]
            filters[2].coords[1] = facial_coords[4][1]
            filters[2].fixate()
            filters[2].paste_filter()

        if(filters_arr[1]):
            filters[0].coords[0] = facial_coords[3][0]
            filters[0].coords[1] = facial_coords[3][1]
            filters[0].img = filters[2].image_after_filter
            filters[0].fixate()
            filters[0].paste_filter()

        if(filters_arr[2]):
            filters[1].coords[0] = facial_coords[2][0]
            filters[1].coords[1] = facial_coords[2][1]
            filters[1].img = filters[0].image_after_filter
            filters[1].fixate()
            filters[1].paste_filter()
        """
        #return filters[1].image_after_filter

        return filters[2].image_after_filter

    else:
        print("Face was not found")

if __name__ == '__main__':
    main()