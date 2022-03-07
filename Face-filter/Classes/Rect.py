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

    def calc_rect_value(self, mini_grid):
        #use integral image to calc the value
        #returns the value of the rect

        w = mini_grid[int(self.x) - 1][int(self.y) - 1] if (int(self.x) > 0 and int(self.y) > 0) else 0
        x = mini_grid[int(self.x) + int(self.width) - 1][int(self.y) - 1] if (int(self.y) > 0) else 0
        y = mini_grid[int(self.x) - 1][int(self.y) + int(self.height) - 1] if (int(self.x) > 0) else 0
        z = mini_grid[int(self.x) + int(self.width) - 1][int(self.y) + int(self.height) - 1]
        value = ( z - x - y + w) / (self.width * self.height)#returns the average sum of the rectangle
        return value 