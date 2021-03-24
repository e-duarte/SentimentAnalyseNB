from load_data import load_texts
from query import count_spc_per_review, spc_per_sentiment
from pre_processing import remove_special_character

if __name__ == '__main__':
    db = load_texts()
    db.to_csv('original.csv')

    db_no_spc = remove_special_character(db)
    db_no_spc.to_csv('special_removed.csv')

    # print(df['REVIEWS'].str.find('\*').sum())
    
