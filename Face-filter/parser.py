import xmlschema

data_schema = xmlschema.XMLSchema('xml/frontal_face.xsd')
data = data_schema.to_dict('xml/frontal_face')
stages = data['haarcascade_frontalface_alt2']['stages']['_']
feature_counter = 0
rects_counter = 0
stages_counter = 0
for stage in stages:
    print("Stage#" , stages_counter)
    trees = stage['trees']
    for tree in trees['_']:
        for treenode in tree['_']:
            print("Feature #", feature_counter)
            feature = treenode['feature']
            threshold = treenode['threshold']
            try:
                left_val = treenode['left_val']
                print("left_val: ",left_val)
            except KeyError:
                left_node = treenode['left_node']
                print("left_node: ",left_node)
            try:
                right_val = treenode['right_val']
                print("right_val: ",right_val)
            except KeyError:
                right_node = treenode['right_node']
                print("right_node: ",right_node)
            print("threshold: ",threshold)
            feature_counter = feature_counter + 1
            rects = feature['rects']
            rects_list = rects['_']
            tilted = feature['tilted']
            print("Tilted: ", tilted)
            for mini in rects_list:
                print("Rect#", rects_counter, mini)
                rects_counter += 1
            rects_counter = 0
    feature_counter = 0
    stages_counter += 1


