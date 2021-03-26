import pandas as pd
import numpy as np


def bag_of_words(db):
    bag = []

    for review in db.REVIEW:
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

        entropy_h = .0
        for c in range(self.n_classes):
            entropy_h += probs[c]*log2s[c]
        
        return entropy_h
        
    def cond_prob(self, apri, post):
        apri = str(apri)
        post = str(post)

        apri  = f'\{apri}' if apri == '?' else apri
        # apri = f'\{apri}' if apri.find('$') == 0 else apri

        amostral_space = self.dataset[self.dataset.REVIEWS.str.match(
            f'.*( ){apri}.*( )|^({apri})( ).*|.*( )({apri}$)|^({apri})$'
        ,) == True]

        post_space = amostral_space[amostral_space.LABEL == post]

        return len(post_space)/len(amostral_space)


    def cond_prob_complement(self, apri, post):
        apri = str(apri)
        post = str(post)

        apri  = f'\{apri}' if apri == '?' else apri
        # apri = f'\{apri}' if apri.find('$') == 0 else apri

        amostral_space = self.dataset.drop(self.dataset[self.dataset.REVIEWS.str.match(
            f'.*( ){apri}.*( )|^({apri})( ).*|.*( )({apri}$)|^({apri})$'
        ,) == True].index)

        post_space = amostral_space[amostral_space.LABEL == post]

        return len(post_space)/len(amostral_space)
    
    def entropy_ngrama(self, apri):
        probs = np.zeros(self.n_classes, dtype='float64')

        for c in range(self.n_classes):
            probs[c] = self.cond_prob(apri, c)
        
        log2s = np.log2(probs, out=np.zeros_like(probs), where=(probs!=0))

        entropy_ngrama = .0
        for c in range(self.n_classes):
            entropy_ngrama += probs[c]*log2s[c]
        
        prob_ngrama = self.prob_review(apri)
        entropy_ngrama = prob_ngrama*entropy_ngrama

        #complement

        complement_prob = np.zeros(self.n_classes, dtype='float64')
        for c in range(self.n_classes):
            complement_prob[c] = self.cond_prob_complement(apri, c)

        complement_log2s = np.log2(complement_prob, out=np.zeros_like(complement_prob), where=(complement_prob!=0))

        c_entropy_ngrama = .0
        for c in range(self.n_classes):
            c_entropy_ngrama += complement_prob[c]*complement_log2s[c]
        
        c_entropy_ngrama = (1 - prob_ngrama)*c_entropy_ngrama

        return entropy_ngrama + c_entropy_ngrama

    def gain(self):
        gain_words = {'word':[], 'gain':[]}

        for word in self.bag:
            gain_words['word'].append(word)
            gain_words['gain'].append(-self.H() + self.entropy_ngrama(word))

        
        return pd.DataFrame(gain_words)

        

            
            

