"""
This is a face detection classifier based on the haar-cascade algorithm.

Contains the stages.

Contains the main classification function that goes through the features.
"""
from Classes.Stage import *
from Constants import const_nums
import cv2
import time


class ClassifierCascade:
    def __init__(self, stages):
        #should it get the stages as an argument or should it extract it here?
        self.stages = stages
        self.mini_grid = [[]]

    def detect_face(self, image):
        counter = 0
        is_face = False
        faces_list = []

        #self.mini_grid = image.arr[start_row:end_row, start_col:end_col]
        start_coords = [0, 0]
        for col in range(const_nums.COLS - 24):
            # if is_face:
            #     break
            for row in range(const_nums.ROWS - 24):
                self.mini_grid = image.arr[row:row+24, col:col+24]
                image.draw_mini_grid((row, col), (row + 24, col + 24))
                start_coords[0] = row
                start_coords[1] = col
                #print("NEW GRID")
                if(self.run_stages(image,start_coords)):
                    #print("FACE!!!")
                    #image.print_og_image_face(row, col)
                    faces_list.append([row, col])

                    #return True
                    is_face = True
                    #toc = time.perf_counter()
                    #print("Detected face in " + str(toc) + " seconds")
                    #break
                else:
                    #print("Next mini_grid")

                    #print("Grid #" + str(counter))
                    counter += 1
        #this function should detect the face
        #mini_grid = 0,0
        #for rows_image
        #for cols_image
        if is_face:
            avrg_coords = self.calc_average_coords(faces_list)
            image.print_og_image_face(avrg_coords[0], avrg_coords[1])
        return is_face

    def calc_average_coords(self, faces_list):
        sum_x =0
        sum_y =0

        for face in faces_list:
            sum_x+=face[0]
            sum_y+=face[1]
        return [sum_x / len(faces_list), sum_y / len(faces_list)]

    def run_stages(self, image, start_coords):
        #goes through all the stages (calls function run_features)
        #and all the features in each stage
        #and returns if a face was detected
        #if the first stage didn't succeed return false

        #stages_list = self.stages[0:3]

        for stage in self.stages[0:3]:
            #print("Stage count: ",stage.count)
            if not stage.run_features(self.mini_grid, image, start_coords):
                return False
            #image.print_stage_num(stage.count)

        return True


