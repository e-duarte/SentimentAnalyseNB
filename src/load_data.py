from os import read
import pandas as pd


DIR = 'data/'
SOURCES = ['amazon_cells_labelled.txt', 'imdb_labelled.txt', 'yelp_labelled.txt']

def read_lines_file(path):
    lines = []
    with open(path) as file:
        lines = file.readlines()

    return [line.replace('\n','') for line in lines]



def load_texts():
    paths = [DIR + src for src in SOURCES]

    dbs = [to_dataframe(read_lines_file(path)) for path in paths]

    return pd.concat(dbs, ignore_index=True)

def to_dataframe(lines):
    reviews = []
    labels = []

    for line in lines:
        review, label = line.split('\t')
        reviews.append(review)
        labels.append(label)
    
    return pd.DataFrame({'REVIEW': reviews, 'LABEL': labels})

