from load_data import load_texts
import pre_processing
from features_selection import bag_of_words, InformationGain
from create_dataset import vectorize_features_count
from dataset import Dataset
import pandas as pd
from validation import k_cross_validate
from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import CategoricalNB
from sklearn.metrics import plot_confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sn


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


    threshold = 0.0011
    gain_threshold = gain[gain['gain'] >= threshold]
    #print(gain_threshold)

    features = gain_threshold.sort_values(by=['gain']).word.to_list()

    feature_dataset = vectorize_features_count(db, features)
    feature_dataset.to_json('feature_dataset.json')

    print('TRAINING AND PREDICTING...')
    
    y = feature_dataset['label'].astype('int32')
    X = feature_dataset.drop(columns=['label'])

    # k-fold cross-validation
    gnb = GaussianNB()
    values_k = [10,15,20]
    for k in values_k:
        print(f'Calculing GaussianNB {k}-fold....')
        cv_results = k_cross_validate(clf=gnb, X=X, y=y, k =k)
        print(cv_results)

        sn.heatmap(pd.DataFrame(cv_results['cm'], index = [i for i in "01"],
                  columns = [i for i in "01"]), annot=True, fmt='3.0f')
        plt.show()





    
