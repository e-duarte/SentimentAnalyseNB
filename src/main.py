from load_data import load_texts
from query import count_spc_per_review, spc_per_sentiment

if __name__ == '__main__':
    db = load_texts()
    count = count_spc_per_review(db['REVIEWS'])

    count['LABEL'] = db['LABEL']
    print(spc_per_sentiment(count, '!', '0'))
    
    # count.to_csv('metricas.csv')
    
    # df = count[count['LABEL'] == '1']
    
    # print(df[df['?'] > 0])
    # print(db.iloc[724].to_string())