class Tree:
    def __init__(self, count):
        self.count = count
        self.nodes = []

    def add_node(self, tree_node):
        self.nodes.append(tree_node)