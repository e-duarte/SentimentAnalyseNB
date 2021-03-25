from operator import pos
import numpy as np


def bag_of_words(reviews):
    bag = []

    for review in reviews['REVIEWS']:
        for word in review.split(' '):
            bag.append(word)
    bag = list(dict.fromkeys(bag))

    return bag


class InformationGain:
    def __init__(self, dataset, bag):
        self.dataset = dataset
        self.bag = bag
        self.n_classes =len(self.dataset.drop_duplicates('LABEL', keep='first'))
    
    def prob(self, c):
        c = str(c)
        return len(self.dataset[self.dataset.LABEL == c])/len(self.dataset.LABEL)

    def cond_prob(self, pri, post):
        pri = str(pri)
        post = str(post)

        amostral_space = self.dataset[self.dataset.REVIEWS.str.find(pri) == 0]
        print(amostral_space)
        post_space = amostral_space[amostral_space.LABEL == post]
        print(post_space)

        return len(post_space)/len(amostral_space)

    def H(self):
        probs = np.zeros(self.n_classes)

        for c in range(self.n_classes):
            probs[c] = self.prob(c)
        
        log2s = np.log2(probs)
        print(log2s)

        entropy_h = .0
        for c in range(self.n_classes):
            entropy_h += probs[c]*log2s[c]
        
        return -entropy_h

        
            
            

