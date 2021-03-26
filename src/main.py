from types import prepare_class
from load_data import load_texts
from query import count_spc_per_review, spc_per_sentiment
import pre_processing
from features_selection import bag_of_words, InformationGain
from create_dataset import vetorize_features
import pandas as pd


def save_features(word):
    with open('src/features.txt', mode='w') as file:
        for w in words:
            file.write(f'{w}\n')

if __name__ == '__main__':
    db = load_texts()
    db.to_csv('original.csv')
    db.REVIEW = pre_processing.lower(db.REVIEW)
    db.REVIEW = pre_processing.remove_special_character(db.REVIEW)
    db.REVIEW = pre_processing.separable_punctuation(db.REVIEW)
    db.REVIEW = pre_processing.remove_stopwords(db.REVIEW)
    db.REVIEW = pre_processing.concat_words(db.REVIEW)
    db.dropna()
    db.to_csv('preprocessed.csv')
    

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

    # with open('src/features.txt', 'r') as file:
    #     features = file.readlines()
    #     features = [i.replace('\n','') for i in features]

    # new_db = vetorize_features(db, features)
    # new_db.to_csv('new_db.csv')
    
    



    
