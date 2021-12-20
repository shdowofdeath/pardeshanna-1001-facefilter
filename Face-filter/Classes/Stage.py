"""
This is a class of a stage.

Contains the stage threshold and the list of trees in the stage
"""

class Stage:
    def __init__(self, count, threshold):
        self.count = count
        self.threshold = threshold
        self.trees = []

    def add_tree(self, tree):
        self.trees.append(tree)

