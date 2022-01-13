"""
This is a face detection classifier based on the haar-cascade algorithm.

Contains the stages.

Contains the main classification function that goes through the features.
"""
from Classes.Stage import *

class ClassifierCascade:
    def __init__(self, stages):
        #should it get the stages as an argument or should it extract it here?
        self.stages = stages
        self.mini_grid = [[]]

    def detect_face(self, image):
        start_row =0
        end_row = 24
        start_col = 0
        end_col = 24
        self.mini_grid = image.arr[start_row:end_row, start_col:end_col]
        #image.draw_mini_grid((0,0), (24,24))
        if(self.run_stages()):
            print("FACE!!!")
        else:
            print("NO!!!!")
        #this function should detect the face
        #mini_grid = 0,0
        #for rows_image
        #for cols_image
        pass

    def run_stages(self):
        #goes through all the stages (calls function run_features)
        #and all the features in each stage
        #and returns if a face was detected
        #if the first stage didn't succeed return false

        for stage in self.stages:
            if not stage.run_features(self.mini_grid):
                return False

        return True
