import pandas as pd


def init_dict_features(features):
    list_dic = []
    for feature in features:
        list_dic.append((feature,[]))
    list_dic.append(('label', []))

    return dict(list_dic)

def vectorize_features_count(dataset, features):
    print('Creating the vectorized datase for frequency')
    
    dic_db = init_dict_features(features)

    labels = dataset['LABEL'].tolist()
    for review, label in zip(dataset['REVIEW'], labels):
        for feature in features:
            words = str(review).split(' ')
            dic_db[feature].append(words.count(feature))
        dic_db['label'].append(label)
    
    return pd.DataFrame(data=dic_db)