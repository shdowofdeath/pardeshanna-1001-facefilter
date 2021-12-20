"""
This is a class of a haar feature.

Contains the rects of the feature

Contains the tilt of the feature
"""

class Feature:
    def __init__(self, is_tilted):
        self.rects = []
        self.is_tilted = is_tilted

    def add_rect(self, rect):
        self.rects.append(rect)