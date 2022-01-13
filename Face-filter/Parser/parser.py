from Classes.Stage import *
from Classes.TreeNode import *
from Classes.Tree import *
from Classes.Feature import *
from Classes.Rect import *
import xmlschema

"""
This function extracts the information from the XML into the classes
"""


def load_stages():
    data_schema = xmlschema.XMLSchema('./xml/frontal_face.xsd')
    data = data_schema.to_dict('xml/frontal_face')
    stages = data['haarcascade_frontalface_alt2']['stages']['_']

    stage_list = []
    tree_counter = 0
    stages_counter = 0

    #goes through the stages
    for stage in stages:
        #builds stage
        _stage = Stage(stages_counter, stage['stage_threshold'])

        #gets the trees from the XML
        trees = stage['trees']

        #goes through the trees
        for tree in trees['_']:

            #builds tree
            _tree = Tree(tree_counter)

            #goes through the treenodes
            for treenode in tree['_']:

                #gets the feature from the XML
                feature = treenode['feature']

                #checks weather there is a value or a node
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

                #builds tree node
                _tree_node = TreeNode(treenode['threshold'], left, right)

                #builds feature
                _feature = Feature(feature['tilted'], treenode['threshold'])

                #gets rects from XML
                rects = feature['rects']
                rects_list = rects['_']

                #goes through the rects
                for rect in rects_list:
                    r = rect.split(' ')
                    #builds rect
                    _rect = Rect(int(r[0]), int(r[1]), int(r[2]), int(r[3]), int(float(r[4])))
                    #adds to feature
                    _feature.add_rect(_rect)

                #adds feature to tree node
                _tree_node.add_feature(_feature)
                #adds tree node to tree
                _tree.add_node(_tree_node)

            #goes to the next tree
            tree_counter += 1
            _stage.add_tree(_tree)
        #goes to the next stage
        tree_counter = 0
        stages_counter += 1
        stage_list.append(_stage)
    return stage_list

