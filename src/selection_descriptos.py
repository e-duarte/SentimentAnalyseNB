
def bag_of_words(reviews):
    bag = []

    for review in reviews['REVIEWS']:
        for word in review.split(' '):
            bag.append(word)
    bag = list(dict.fromkeys(bag))

    return bag

def information_gain(reviews, bag):
    pass