from load_data import load_texts
import pre_processing
from features_selection import bag_of_words, InformationGain
from create_dataset import vectorize_features_count
from dataset import Dataset
import pandas as pd


if __name__ == '__main__':
    db = load_texts()
    db.to_csv('original.csv')
    db.REVIEW = pre_processing.lower(db.REVIEW)
    db.REVIEW = pre_processing.separable_punctuation(db.REVIEW)
    db.REVIEW = pre_processing.remove_special_character(db.REVIEW)
    db.REVIEW = pre_processing.remove_stopwords(db.REVIEW)
    db.REVIEW = pre_processing.concat_words(db.REVIEW)
    db.dropna()
    db.to_csv('preprocessed.csv')

    dt = Dataset(db.REVIEW, db.LABEL)


    # bag-of-word 1-grama
    print('GET BAG OF WORDS')
    bag = bag_of_words(db)

    print('CALCULING THE INFORMATION GAIN...')
    gain = InformationGain(dt, bag).gain()

    gain = gain[gain['gain'] >= 0.001]
    print(gain)

    gain.to_csv('gain.csv')
    # # print(db_preprocessing[db_preprocessing.REVIEWS.str.find('not') == 0])

    # df = pd.read_csv('gain.csv')
    # words = df[df['gain'] >= 0.003].sort_values(by=['gain']).word.to_list()

    # with open('src/features.txt', 'r') as file:
    #     features = file.readlines()
    #     features = [i.replace('\n','') for i in features]




    
