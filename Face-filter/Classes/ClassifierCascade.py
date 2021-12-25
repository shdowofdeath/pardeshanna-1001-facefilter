"""
This is a face detection classifier based on the haar-cascade algorithm.

Contains the stages.

Contains the main classification function that goes through the features.
"""

class ClassifierCascade:
    def __init__(self, stages):
        #should it get the stages as an argument or should it extract it here?
        self.stages = stages

    def detect_face(self, image):
        #this function should detect the face
        #mini_grid = 0,0
        #for rowS_image
            #for cols_image

        pass

    def run_stages(self, mini_grid):
        #goes through all the stages (calls function run_features)
        #and all the features in each stage
        #and returns if a face was detected
        #if the first stage didn't succeed return false
        pass
