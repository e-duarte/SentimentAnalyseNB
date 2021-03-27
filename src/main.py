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
    # db.to_csv('preprocessed.csv')

    # dt = Dataset(db.REVIEW, db.LABEL)

    # # # bag-of-word 1-grama
    # print('GET BAG OF WORDS')
    # bag = bag_of_words(db)

    # print('CALCULING THE INFORMATION GAIN...')
    # gain = InformationGain(dt, bag).gain()
    # gain.to_csv('gain.csv')

    '''load information gain per word'''
    gain = pd.read_csv('gain.csv')


    threshold = 0.005
    gain_threshold = gain[gain['gain'] >= threshold]
    print(gain_threshold)

    features = gain_threshold.sort_values(by=['gain']).word.to_list()

    feature_dataset = vectorize_features_count(db, features)
  
    





    
