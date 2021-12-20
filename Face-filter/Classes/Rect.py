"""
This is a class of a rect which is contained in the haar feature.

Contains the coordinates of the rect, the width and the height
"""

class Rect:
    def __init__(self, x, y, width, height, weight):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.weight = weight
