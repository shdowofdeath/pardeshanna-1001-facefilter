"""
This is a class of Tree.

Contains the tree nodes and the count of the tree
"""
from Classes.TreeNode import *
class Tree:
    def __init__(self, count):
        self.count = count
        self.nodes = []

    def add_node(self, tree_node):
        self.nodes.append(tree_node)