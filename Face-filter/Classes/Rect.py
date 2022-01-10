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

        w = mini_grid[self.x - 1][self.y - 1] if (self.x > 0 and self.y>0) else 0
        x = mini_grid[self.x][self.y - 1] if (self.y > 0) else 0
        y = mini_grid[self.x - 1][self.y] if (self.x > 0) else 0
        z = mini_grid[self.x + self.width - 1][self.y +self.height - 1]
        return z - x - y + w