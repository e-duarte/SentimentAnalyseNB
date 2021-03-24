import pandas as pd

#spc: special character . ! : ; ?
def count_spc_per_review(reviews):
    special_character = ['!', '\?']
    
    count_per_reviews = []

    for spc in special_character:
        count_per_reviews.append(reviews.str.count(spc))
    
    counting = pd.DataFrame()
    
    for spc, serie in zip(['!', '?'], count_per_reviews):
        counting[spc] = serie

    return counting

def spc_per_sentiment(count_spc, spc='!', sentiment='0'):
     df = count_spc[count_spc['LABEL'] == sentiment]
     return df[df[spc] > 0]
     