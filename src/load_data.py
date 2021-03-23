from os import read
import pandas as pd


def load_texts():
    sources = ['amazon_cells_labelled.txt', 'imdb_labelled.txt', 'yelp_labelled.txt']

    dbs = []

    for txt in sources:
        with open("data/"+txt) as file:
            dbs.append(to_dataframe(file.readlines()))


    return pd.concat(dbs, ignore_index=True)

def to_dataframe(lines):
    reviews = []
    labels = []

    for line in lines:
        line = line.replace('\n', '')
        review, label = line.split('\t')
        reviews.append(review)
        labels.append(label)
    
    
    return pd.DataFrame({'REVIEWS': reviews, 'LABEL': labels})

