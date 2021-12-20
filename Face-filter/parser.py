import xmlschema
from Classes.Stage import *
from Classes.TreeNode import *
from Classes.Tree import *
from Classes.Feature import *
from Classes.Rect import *

def load_stages():
    data_schema = xmlschema.XMLSchema('xml/frontal_face.xsd')
    data = data_schema.to_dict('xml/frontal_face')
    stages = data['haarcascade_frontalface_alt2']['stages']['_']

    stage_list = []
    tree_counter = 0
    stages_counter = 0

    for stage in stages:
        _stage = Stage(stages_counter, stage['stage_threshold'])

        trees = stage['trees']
        for tree in trees['_']:
            _tree = Tree(tree_counter)
            for treenode in tree['_']:

                feature = treenode['feature']

                try:
                    left_val = treenode['left_val']
                    left = left_val
                except KeyError:
                    left_node = treenode['left_node']
                    left = left_node
                try:
                    right_val = treenode['right_val']
                    right = right_val
                except KeyError:
                    right_node = treenode['right_node']
                    right = right_node

                _tree_node = TreeNode(treenode['threshold'], left, right)

                _feature = Feature(feature['tilted'])

                rects = feature['rects']
                rects_list = rects['_']

                for rect in rects_list:
                    r = rect.split(' ')
                    _rect = Rect(int(r[0]), int(r[1]), int(r[2]), int(r[3]), 0)
                    _feature.add_rect(_rect)

                _tree_node.add_feature(_feature)
                _tree.add_node(_tree_node)
            tree_counter += 1
            _stage.add_tree(_tree)
        tree_counter = 0
        stages_counter += 1
        stage_list.append(_stage)
    return stage_list

stages = load_stages()
print(stages)
