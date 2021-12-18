from const_libraries import *

class Stage:
    def __init__(self, count, threshold):
        self.count = count
        self.threshold = threshold
        self.classifier = []

class Classifier:
    def __init__(self, count, alpha, node):
        self.count = count
        self.alpha = alpha
        self.node = node

class TreeNode:
    def __init__(self, threshold, left, right, feature):
        self.threshold = threshold
        self.left = left
        self.right = right
        self.feature = feature

class Feature:
    def __init__(self, x, y, width, height, weight):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.weight = weight

