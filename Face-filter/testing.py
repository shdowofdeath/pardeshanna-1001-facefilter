import xmlschema

data_schema = xmlschema.XMLSchema('better.xsd')
data = data_schema.to_dict('better')
stages = data['haarcascade_frontalface_alt2']['stages']['_']
feature_counter = 0
rects_counter = 0
stages_counter = 0
for stage in stages:
    print("Stage#" , stages_counter)
    trees = stage['trees']
    for tree in trees['_']:
        #treenodes = tree
        for treenode in tree['_']:
            feature = treenode['feature']
            threshold = treenode['threshold']
            #left_val = treenode['left_val']
            #right_val = treenode['right_val']
            print("Feature #" , feature_counter)
            #print("rects: ", feature)
            print("threshold: ",threshold)
            #print("left_val: ",left_val)
            #print("right_val: ",right_val)
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


