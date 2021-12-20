class TreeNode:
    def __init__(self, threshold, left, right):
        self.feature = None
        self.threshold = threshold
        self.left = left
        self.right = right

    def add_feature(self, feature):
        self.feature = feature