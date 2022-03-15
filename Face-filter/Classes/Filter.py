from Classes.Image import *
from PIL import Image as Im


class Filter:
    def __init__(self, filterImage, img, name):
        self.filterImage = filterImage
        self.coords = [0,0]
        self.img = img
        self.name = name
        self.image_after_filter = None



    def paste_filter(self):
        '''
        Takes the image and pastes the filter image on top of it
        saves the new filtered image as the image
        '''
        background = copy.copy(self.img)#copies the original image to the background
        foreground = copy.copy(self.filterImage)#copies the filter image as the foreground
        background.paste(foreground, (self.coords[0], self.coords[1]), foreground)#pastes the filter on top of the original image
        self.image_after_filter = background#saves new image


class Glasses(Filter):
    def __init__(self, filterImage, img, name):
        Filter.__init__(self, filterImage, img, name)
        self.filterImage = self.filterImage.resize((170, 60))

    def fixate(self):
        #fixes the position of the filter image
        self.coords[0] -= (self.filterImage.width) // 2
        self.coords[1] -= 20

class Lips(Filter):
    def __init__(self, filterImage, img, name):
        Filter.__init__(self, filterImage, img, name)
        self.filterImage = self.filterImage.resize((110, 90))

    def fixate(self):
        # fixes the position of the filter image
        self.coords[0] -= 35#x coord
        self.coords[1] -= 40#y coord

class Hat(Filter):
    def __init__(self, filterImage, img, name):
        Filter.__init__(self, filterImage, img, name)

    def fixate(self):
        # fixes the position of the filter image
        self.coords[0] -= 50#x coord
        self.coords[1] -= 130#y coord
        self.filterImage = self.filterImage.resize((100, 100))

def filterCreator(img):
    '''
    This function creates a list of filters of different kinds
    '''
    filters = []
    filters.append(Glasses(Im.open("Filters/glasses.png").convert("RGBA"), img, "glasses"))
    filters.append(Lips(Im.open("Filters/lips_2.png").convert("RGBA"), img,"lips"))
    filters.append(Hat(Im.open("Filters/witch-hat.png").convert("RGBA"), img, "witch_hat"))

    return filters