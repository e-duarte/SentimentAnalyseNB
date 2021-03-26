import pandas as pd

def vetorize_features(dataset, features):
    list_dic = []
    for feature in features:
        list_dic.append((feature,[]))
    list_dic.append(('label', []))
    dic_db = dict(list_dic)

    labels = dataset['LABEL'].tolist()
    for review, label in zip(dataset['REVIEWS'], labels):
        for feature in features:
            review = str(review).split(' ')
            dic_db[feature].append(review.count(feature))
        dic_db['label'].append(label)
    
    return pd.DataFrame(data=dic_db)