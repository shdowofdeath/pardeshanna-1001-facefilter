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
        self.stages = stages
        self.mini_grid = [[]]

    def detect_face(self, image):
        is_face = False
        faces_list = []
        start_coords = [0, 0]

        for col in range(const_nums.COLS - const_nums.MINI_GRID_SIZE):
            for row in range(const_nums.ROWS - const_nums.MINI_GRID_SIZE):
                self.mini_grid = image.arr[row:row+const_nums.MINI_GRID_SIZE, col:col+const_nums.MINI_GRID_SIZE]#gets the mini grid
                image.draw_mini_grid((row, col), (row + const_nums.MINI_GRID_SIZE, col + const_nums.MINI_GRID_SIZE))
                start_coords[0] = row
                start_coords[1] = col
                if(self.run_stages(image,start_coords)):#run stages in mini grid
                    #face found
                    faces_list.append([row, col])
                    is_face = True

        if is_face:#face found
            avrg_coords = self.calc_average_coords(faces_list)#gets the average coords of the face

        return is_face, avrg_coords

    def calc_average_coords(self, faces_list):
        #returns the average coordinates of the faces found
        sum_x = 0
        sum_y = 0

        for face in faces_list:#goes through the faces coordinates
            #adds coords to sum
            sum_x += face[0]
            sum_y += face[1]
        return [int(sum_x / len(faces_list)), int(sum_y / len(faces_list))]#returns the average coords

    def run_stages(self, image, start_coords):
        for stage in self.stages[0:3]:#goes through the stages
            if not stage.run_features(self.mini_grid, image, start_coords):#runs the features in each stage
                return False#no face found

        return True#face found


