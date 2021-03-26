from os import remove
import re

special_characters = [
        '`',
        '-',
        '~',
        '^',
        # '\'',
        '\"',
        ',',
        '\[...\]',
        '.',
        ';',
        ':'
        # '?',
        # '!',
        '@',
        '#',
        '$',
        '+',
        '*',
        '\\',
        '/',
        '\(',
        '\)',
        '&',
        ':\)',
        ';\)',
        ':D',
        ':\(',
        ';\(',
        ':1\)'
    ]

def remove_additional_space(reviews):
    reviews.REVIEWS = reviews.REVIEWS.str.strip()
    reviews.REVIEWS = reviews.REVIEWS.str.replace(' +', ' ', regex=True)
    return reviews
def remove_special_character(reviews):
    for scp in special_characters:
        reviews['REVIEWS'] = reviews['REVIEWS'].str.replace(scp, ' ') #remove spc
        reviews['REVIEWS'] = reviews['REVIEWS'].str.replace('  ', ' ') #remove doble space
        reviews['REVIEWS'] = reviews['REVIEWS'].str.replace('!', ' ! ') #remove doble space
        reviews['REVIEWS'] = reviews['REVIEWS'].str.replace('?', ' ? ') #remove doble space
        reviews['REVIEWS'] = reviews['REVIEWS'].str.replace(r'^ | $', '', regex=True) #remove space in the begin and the end of line    
    return remove_additional_space(reviews)

def remove_stopwords(reviews):
    stopwords = []

    with open('src/stopwords.txt') as file:
        stopwords = file.readlines()
    
    for i in range(len(stopwords)):
        stopwords[i] = stopwords[i].replace('\n', '')
    
    for stp in stopwords:
        reviews['REVIEWS'] = reviews['REVIEWS'].str.replace(f' {stp} ', ' ', flags=re.IGNORECASE, regex=True) #stopword
        reviews['REVIEWS'] = reviews['REVIEWS'].str.replace(f'^({stp} )|( {stp})$', '', flags=re.IGNORECASE, regex=True) #stopword
    
    for stp in stopwords:
        reviews.REVIEWS = reviews.REVIEWS.str.replace(f' {stp} ', ' ')
        
    return remove_additional_space(reviews)

def concat_words(reviews):
    words = ['no', 'nothing', 'not']

    for word in words:
        reviews['REVIEWS'] = reviews['REVIEWS'].str.replace(f'({word} )', f'{word}_', flags=re.IGNORECASE, regex=True)

    return remove_additional_space(reviews)

def remove_words_1_len(bag):
    for b in bag:
        if len(b) == 1:
            if not ((b == '?') or ( b == '!')):
                bag.remove(b)
    bag.remove('x')
    return bag