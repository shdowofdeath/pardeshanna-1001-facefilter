from Classes.Rect import *
"""
This is a class of a haar feature.

Contains the rects of the feature

Contains the tilt of the feature
"""

class Feature:
    def __init__(self, is_tilted, threshold):
        self.rects = []
        self.is_tilted = is_tilted
        self.threshold = threshold

    def add_rect(self, rect):
        self.rects.append(rect)

    def is_diff(self, mini_grid, rect1, rect2):
        #get value of rect1
        #get value of rect2
        #calculate the difference between them
        #return if the difference is closer to 1 (1/threshold?)

        rect1_value = rect1.calc_rect_value(mini_grid)
        rect2_value = rect2.calc_rect_value(mini_grid)

        if rect1.weight < 0: #rect 1 is the black
            diff = rect1_value - rect2_value
        else: #rect 2 is the black
            diff = rect2_value - rect1_value

        if diff >= self.threshold:
            return True
        return False

    def is_feature_existent(self, mini_grid, image, start_coords):
        #check the number of rects there are:
        #if there are two => send both to "is_diff" and return if there is a difference
        #if there are three => send two sets of rects to "is_diff" and return if there is a difference in BOTH
        #if there are three => send four sets of rects "is_diff" and return if there is a difference in ALL
        #we are not checking tilted rects or "one in one" rects for now

        if(not self.is_tilted):#handling not tilted
            if len(self.rects) == 2:
                if self.rects[0].x == self.rects[1].x: #lays
                    #y && height
                    if((self.rects[1].y - self.rects[0].y) == (self.rects[0].height - self.rects[1].height)):
                        #2 rects
                        rect1 = Rect(self.rects[0].x, self.rects[0].y, self.rects[0].width, self.rects[0].height / 2, self.rects[0].weight)
                        if(self.is_diff(mini_grid,rect1, self.rects[1])):
                            #success (return true)
                            return True
                        else:
                            #fail
                            return False
                    elif((self.rects[1].y - self.rects[0].y) * 2 == (self.rects[0].height - self.rects[1].height)):
                        #3 rects
                        middle = self.rects[1]
                        above = Rect(self.rects[0].x, self.rects[0].y, self.rects[0].width, self.rects[0].height / 3, self.rects[0].weight)
                        below = Rect(self.rects[0].x, self.rects[1].y + (self.rects[0].height / 3), self.rects[0].width, self.rects[0].height / 3, self.rects[0].weight)
                        if(self.is_diff(mini_grid,above, middle) and self.is_diff(mini_grid,below, middle)):
                            #success
                            return True
                        else:
                            #fail
                            return False
                elif self.rects[0].y == self.rects[1].y: #stands
                    #x && width
                    if ((self.rects[1].x - self.rects[0].x) == (self.rects[0].width - self.rects[1].width)):
                        # 2 rects
                        rect1 = Rect(self.rects[0].x, self.rects[0].y, self.rects[0].width / 2, self.rects[0].height, self.rects[0].weight)
                        if (self.is_diff(mini_grid, rect1, self.rects[1])):
                            # success (return true)
                            return True
                        else:
                            # fail
                            return False
                    elif ((self.rects[1].x - self.rects[0].x) * 2 == (self.rects[0].width - self.rects[1].width)):
                        # 3 rects
                        middle = self.rects[1]
                        left = Rect(self.rects[0].x, self.rects[0].y, self.rects[0].width / 3, self.rects[0].height, self.rects[0].weight)
                        right = Rect(self.rects[1].x + (self.rects[0].width / 3), self.rects[0].y, self.rects[0].width / 3,
                                     self.rects[0].height, self.rects[0].weight)
                        if (self.is_diff(mini_grid, left, middle) and self.is_diff(mini_grid, right, middle)):
                            # success
                            return True
                        else:
                            # fail
                            return False
                else:
                    #one in one
                    pass
            elif len(self.rects) == 3:#there are 4 rects
                if(self.rects[0].x == self.rects[1].x and self.rects[0].y == self.rects[1].y): #same starting point
                    top_left = self.rects[1]
                    top_right = Rect(self.rects[0].x + (self.rects[0].width / 2), self.rects[0].y, self.rects[0].width / 2, self.rects[0].height / 2, self.rects[0].weight)
                    bottom_left = Rect(self.rects[0].x, self.rects[0].y + (self.rects[0].height / 2), self.rects[0].width / 2, self.rects[0].height / 2, self.rects[0].weight)
                    bottom_right = self.rects[2]

                    if self.is_diff(mini_grid, top_left, top_right) and self.is_diff(mini_grid, top_left, bottom_left) and self.is_diff(mini_grid, top_right, bottom_right) and self.is_diff(mini_grid, bottom_left, bottom_right):
                        #success
                        return True
                    else:
                        #fail
                        return False
                else:
                    top_left = Rect(self.rects[0].x, self.rects[0].y, self.rects[0].width / 2, self.rects[0].height / 2, self.rects[0].weight)
                    top_right = self.rects[1]
                    bottom_left = self.rects[2]
                    bottom_right = Rect(self.rects[0].x + (self.rects[0].width / 2), self.rects[0].y + (self.rects[0].height / 2), self.rects[0].width / 2, self.rects[0].height / 2, self.rects[0].weight)

                    if self.is_diff(mini_grid, top_left, top_right) and self.is_diff(mini_grid, top_left, bottom_left) and self.is_diff(mini_grid, top_right, bottom_right) and self.is_diff(mini_grid, bottom_left, bottom_right):
                        #success
                        return True
                    else:
                        #fail
                        return False
