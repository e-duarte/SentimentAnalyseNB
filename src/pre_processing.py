from os import remove
import re
from load_data import read_lines_file

SOURCE_SPC = 'src/special_characters.txt'
SOURCE_STOPWORDS = 'src/stopwords.txt'

special_characters = read_lines_file(SOURCE_SPC)
stopwords = read_lines_file(SOURCE_STOPWORDS)

def lower(lines):
    print('SWITCH LETTERS TO LOWER CASE')
    return [line.lower() for line in lines]

def remove_additional_space(lines):
    print('REMOVING ADDICIONAL SPACE')
    removed_space = [line.strip() for line in lines]
    return [re.sub(' +',  ' ', line) for line in removed_space]

def separable_punctuation(lines):
    print('SEPARARING PUNCTUATIONS IN LINE AS WORD')
    for punct in ['!', '\?']:
        lines = [re.sub(punct, f' {punct} '.replace('\\',''), line) for line in lines]

    return remove_additional_space(lines)
        
def remove_special_character(lines):
    print('REMOVING SPECIAL CHARACTERS FROM "special_characters.txt" FILE')
    lines = remove_additional_space(lines)

    for scp in special_characters:
        lines = [re.sub(scp, '', line) for line in lines]

    return remove_additional_space(lines)

def remove_stopwords(lines):
    print('REMOVING STOPWORDS FROM "stopwords.txt" FILE')

    for stp in stopwords:
        lines = [re.sub(f' {stp} |^({stp}) |( {stp})$', ' ',line) for line in lines]
  
    return remove_additional_space(lines)

def concat_words(lines):
    print('CONCATING WORDS WITH ONLY MEANING')
    words = ['no', 'nothing', 'not', 'dont', "don't", "doesn't", "didn't", "haven't", "hasn't"]

    for word in words:
        lines = [re.sub(f'{word} ', f'{word}_', line) for line in lines]

    return lines