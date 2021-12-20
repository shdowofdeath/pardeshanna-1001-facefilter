#from Classes.Tree import *

class Stage:
    def __init__(self, count, threshold):
        self.count = count
        self.threshold = threshold
        self.trees = []

    def add_tree(self, tree):
        self.trees.append(tree)

