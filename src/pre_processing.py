special_characters = [
        '`',
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

def remove_special_character(reviews):
    for scp in special_characters:
        reviews['REVIEWS'] = reviews['REVIEWS'].str.replace(scp, ' ') #remove spc
        reviews['REVIEWS'] = reviews['REVIEWS'].str.replace('  ', ' ') #remove doble space
        reviews['REVIEWS'] = reviews['REVIEWS'].str.replace(r'^ | $', '', regex=True) #remove space in the begin and the end of line

    return reviews