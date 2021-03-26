from pandas.core.reshape.concat import concat
from load_data import load_texts
from query import count_spc_per_review, spc_per_sentiment
from pre_processing import remove_special_character, remove_stopwords, concat_words, remove_words_1_len
from features_selection import bag_of_words, InformationGain
from create_dataset import vectorize_features_count
import pandas as pd


def save_features(word):
    with open('src/features.txt', mode='w') as file:
        for w in words:
            file.write(f'{w}\n')

if __name__ == '__main__':
    db = load_texts()
    db['REVIEWS'] = db['REVIEWS'].str.lower()
    # # print(db)
    # db.to_csv('original.csv')

    # #pre-processing
    print('PRE-PROCESSING DATASET...')
    db_preprocessing = concat_words(remove_stopwords(remove_special_character(db)))


    # #bag-of-word 1-grama
    # print('GET BAG OF WORDS...')
    # bag = bag_of_words(db_preprocessing)

    # #clean bag of words
    # bag = remove_words_1_len(bag)
    # bag.remove('not')
    # bag.remove('no')
    
    
    # print('CALCULING THE INFORMATION GAIN...')
    # gain = InformationGain(db_preprocessing, bag).gain()
    # print(gain)


    # # # gain = gain[gain['gain'] >= 0.7]

    # gain.to_csv('gain.csv')
    # # print(db_preprocessing[db_preprocessing.REVIEWS.str.find('not') == 0])

    # df = pd.read_csv('gain.csv')
    # words = df[df['gain'] >= 0.003].sort_values(by=['gain']).word.to_list()

    with open('src/features.txt', 'r') as file:
        features = file.readlines()
        features = [i.replace('\n','') for i in features]

    new_db = vectorize_features_count(db, features)
    # new_db.to_csv('new_db.csv')

    
    



    
