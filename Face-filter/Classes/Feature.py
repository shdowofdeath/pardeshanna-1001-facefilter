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

    def is_diff(self, mini_grid, rect1, rect2):
        #get value of rect1
        #get value of rect2
        #calculate the difference between them
        #return if the difference is greater than 1
        pass

    def calc_rects_diff(self):
        #check the number of rects there are:
        #if there are two => send both to "is_diff" and return if there is a difference
        #if there are three => send two sets of rects to "is_diff" and return if there is a difference in BOTH
        #if there are four => send four sets of rects "is_diff" and return if there is a difference in ALL
        #we are not checking tilted rects or "one in one" rects for now
        pass