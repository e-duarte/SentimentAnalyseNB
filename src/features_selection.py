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
    
    def prob_label(self, c):
        c = str(c)
        return len(self.dataset[self.dataset.LABEL == c])/len(self.dataset.LABEL)

    def prob_review(self, t):
        t = str(t)
        return len(self.dataset[self.dataset.REVIEWS.str.find(t) == 0])/len(self.dataset.LABEL)

    def H(self):
        probs = np.zeros(self.n_classes)

        for c in range(self.n_classes):
            probs[c] = self.prob_label(c)
        
        log2s = np.log2(probs)
        print(log2s)

        entropy_h = .0
        for c in range(self.n_classes):
            entropy_h += probs[c]*log2s[c]
        
        return entropy_h
        
    def cond_prob(self, apri, post):
        pri = str(apri)
        post = str(post)

        amostral_space = self.dataset[self.dataset.REVIEWS.str.find(apri) == 0]
        # print(amostral_space)
        post_space = amostral_space[amostral_space.LABEL == post]
        # print(post_space)

        return len(post_space)/len(amostral_space)
    
    def entropy_ngrama(self, pri):
        probs = np.zeros(self.n_classes)

        for c in range(self.n_classes):
            probs[c] = self.cond_prob(pri, c)
        
        log2s = np.log2(probs)

        entropy_ngrama = .0
        for c in range(self.n_classes):
            entropy_ngrama += probs[c]*log2s[c]
        
        prob_ngrama = self.prob_review(pri)
        entropy_ngrama = prob_ngrama*entropy_ngrama

        complement_prob = 1 - probs
        complement_log2s = np.log2(complement_prob)

        print(complement_log2s)
        print(complement_prob)
        exit()

        c_entropy_ngrama = .0
        for c in range(self.n_classes):
            c_entropy_ngrama += complement_prob[c]*complement_log2s[c]
        
        c_entropy_ngrama = (1 - prob_ngrama)*c_entropy_ngrama

        return entropy_ngrama + c_entropy_ngrama

    def gain():
        pass
        

            
            

