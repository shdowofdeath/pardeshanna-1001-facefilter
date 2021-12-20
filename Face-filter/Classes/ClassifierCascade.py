"""
This is a face detection calssifier based on the haar-cascade algorithm.

Contains the stages.

Contains the main classification function that goes through the features.
"""

class ClassifierCascade:
    def __init__(self, stages):
        #shoudl it get the stages as an argument or should it extract it here?
        self.stages = stages

    def detect_face(self, image):
        pass
