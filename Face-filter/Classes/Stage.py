"""
This is a class of a stage.

Contains the stage threshold and the list of trees in the stage
"""
from Classes.Tree import *
from Classes.Feature import *

class Stage:
    def __init__(self, count, threshold):
        self.count = count
        self.threshold = threshold
        self.trees = []

    def add_tree(self, tree):
        self.trees.append(tree)

    def run_features(self, mini_grid):
        threshold = 0
        node_counter = 0
        for tree in self.trees:
            for node in tree:
                if node.feature.is_feature_existent(mini_grid):
                    if node.right != 1:#stop traversing nodes add val to threshold
                        threshold += node.right
                else:
                    if node.left != 1:#stop traversing nodes add val to threshold
                        threshold += node.left
        if threshold >= self.threshold:
            return True
        else:
            return False
