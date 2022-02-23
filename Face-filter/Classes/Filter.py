import copy
from Classes.Image import *
from Classes.EdgeDetection import *
from Classes.ClassifierCascade import *
from Parser.parser import load_stages
from Constants import const_nums
import time
from PIL import Image as Im, ImageDraw, ImageFilter

class Filter:
    def __init__(self, filterImage, img, name):
        self.filterImage = filterImage
        self.coords = [0,0]
        self.img = img
        self.name = name
        self.image_after_filter = None

    def resize(self, width, height):
        self.filterImage = self.filterImage.resize((70, 20))

    """
    takes the image and pastes the filter image on top of it
    saves the new filtered image as the image
    """
    def paste_filter(self):
        background = copy.copy(self.img)
        foreground = copy.copy(self.filterImage)
        print(self.coords[0], self.coords[1])
        background.paste(foreground, (self.coords[0], self.coords[1]), foreground)
        self.image_after_filter = background


class Glasses(Filter):
    def __init__(self, filterImage, img, name):
        Filter.__init__(self, filterImage, img, name)
        self.filterImage = self.filterImage.resize((170, 60))

    def fixate(self):
        self.coords[0] -= (self.filterImage.width) // 2
        self.coords[1] -= 20

class Lips(Filter):
    def __init__(self, filterImage, img, name):
        Filter.__init__(self, filterImage, img, name)
        self.filterImage = self.filterImage.resize((110, 60))

    def fixate(self):
        self.coords[0] -= 20#(self.coords[0].filterImage.width) // 2
        self.coords[1] -= 20#10

class Hat(Filter):
    def __init__(self, filterImage, img, name):
        Filter.__init__(self, filterImage, img, name)

    def fixate(self):
        self.coords[0] -= 70#(self.coords[0].filterImage.width) // 2
        self.coords[1] -= 130#10
        self.filterImage = self.filterImage.resize((100, 100))

def filterCreator(img):
    filters = []

    filters.append(Glasses(Im.open("Filters/glasses.png").convert("RGBA"), img, "glasses"))
    filters.append(Lips(Im.open("Filters/lips.png").convert("RGBA"), img,"lips"))
    filters.append(Hat(Im.open("Filters/witch-hat.png").convert("RGBA"), img, "witch_hat"))
    return filters