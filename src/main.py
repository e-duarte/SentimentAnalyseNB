from pandas.core.reshape.concat import concat
from load_data import load_texts
from query import count_spc_per_review, spc_per_sentiment
from pre_processing import remove_special_character, remove_stopwords, concat_words
from features_selection import bag_of_words, InformationGain

if __name__ == '__main__':
    db = load_texts()

    #pre-processing
    print('PRE-PROCESSING DATASET...')
    db_preprocessing = concat_words(remove_stopwords(remove_special_character(db)))
    
    db_preprocessing.to_csv('teste.csv')
    # db_no_stp = remove_stopwords(db_no_spc)
    # db_concat = concat_words(db_no_stp)

    #bag-of-word 1-grama
    print('GET BAG OF WORDS...')
    bag = bag_of_words(db_preprocessing)
    
    print(InformationGain(db_preprocessing, bag).entropy_ngrama('no_way'))
    # print(db_preprocessing[db_preprocessing.REVIEWS.str.find('not') == 0])

    


    
