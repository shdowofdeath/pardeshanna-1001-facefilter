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

    def paste_filter(self):
        background = copy.copy(self.img)
        foreground = copy.copy(self.filterImage)
        #alpha = foreground.convert('RGBA')
        print(self.coords[0], self.coords[1])
        background.paste(foreground, (self.coords[0], self.coords[1]), foreground)
        self.image_after_filter = background


class Glasses(Filter):
    def __init__(self, filterImage, img, name):
        Filter.__init__(self, filterImage, img, name)
        self.filterImage = self.filterImage.resize((170, 60))

    def fixate_glasses(self):
        self.coords[0] -= (self.filterImage.width) // 2
        self.coords[1] -= 10

class Lips(Filter):
    def __init__(self, filterImage, img, name):
        Filter.__init__(self, filterImage, img, name)
        self.filterImage = self.filterImage.resize((100, 60))

    def fixate_lips(self):
        self.coords[0] -= 20#(self.coords[0].filterImage.width) // 2
        self.coords[1] -= 20#10

class Hat(Filter):
    def __init__(self, filterImage, img, name):
        Filter.__init__(self, filterImage, img, name)

    def fixate_hat(self):
        self.coords[0] -= 60#(self.coords[0].filterImage.width) // 2
        self.coords[1] -= 90#10
        self.filterImage = self.filterImage.resize((100, 100))

def filterCreator(img):
    filters = []

    filters.append(Glasses(Im.open("Filters/glasses.png").convert("RGBA"), img, "glasses"))
    filters.append(Lips(Im.open("Filters/lips.png").convert("RGBA"), img,"lips"))
    filters.append(Hat(Im.open("Filters/witch-hat.png").convert("RGBA"), img, "witch_hat"))
    return filters