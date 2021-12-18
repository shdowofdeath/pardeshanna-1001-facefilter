import xmlschema

data_schema = xmlschema.XMLSchema('features.xsd')
data = data_schema.to_dict('xmlFile')
stages = data['stages']['_']
feature_counter = 0
rects_counter = 0
stages_counter = 0
for stage in stages:
    print("Stage#" , stages_counter)
    trees = stage['trees']
    for tree in trees['_']:
        features = tree['_']
        feature = features['feature']
        threshold = features['threshold']
        left_val = features['left_val']
        right_val = features['right_val']
        print("Feature #" , feature_counter)
        #print("rects: ", feature)
        print("threshold: ",threshold)
        print("left_val: ",left_val)
        print("right_val: ",right_val)
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


