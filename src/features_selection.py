import numpy as np
import pandas as pd

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
        self.n_classes =len(self.dataset.dataset.drop_duplicates('LABEL', keep='first'))
    
    def prob(self, c, column):
        c_space = self.dataset.find_x_column(c, column)

        amostral_space = self.dataset.dataset.LABEL

        return len(c_space)/len(amostral_space)

    def entropy(self):
        probs = np.zeros(self.n_classes)

        for c in range(self.n_classes):
            probs[c] = self.prob(str(c), 'LABEL')
        
        log2s = np.log2(probs)

        entropy_h = .0
        for c in range(self.n_classes):
            entropy_h += probs[c]*log2s[c]
        
        return entropy_h
        
    def cond_prob(self, posteriori, priori, column1, column2, neg=False):
        amostral_space = None
        post_space = None
        if not neg:
            amostral_space = self.dataset.find_x_column(priori, column2)
            post_space = self.dataset.find_x_y_column(priori, posteriori, column2, column1)
        else:
            amostral_space = self.dataset.find_x_neg_column(priori, column2)
            post_space = self.dataset.find_x_y_neg_column(priori, posteriori, column2, column1)

        return len(post_space)/len(amostral_space)

    
    def entropy_ngrama(self, priori):
        probs = np.zeros(self.n_classes, dtype='float64')

        for c in range(self.n_classes):
            probs[c] = self.cond_prob(
                posteriori=str(c),
                priori=priori,
                column1='LABEL',
                column2='REVIEW'
            )
        
        log2s = np.log2(probs, out=np.zeros_like(probs), where=(probs!=0))

        entropy_ngrama = .0
        for c in range(self.n_classes):
            entropy_ngrama += probs[c]*log2s[c]
        
        prob_ngrama = self.prob(priori, 'REVIEW')
        entropy_ngrama = prob_ngrama*entropy_ngrama


        #complement

        complement_prob = np.zeros(self.n_classes, dtype='float64')
        for c in range(self.n_classes):
            complement_prob[c] = self.cond_prob(
                posteriori=str(c),
                priori=priori,
                column1='LABEL',
                column2='REVIEW',
                neg=True
            )

        complement_log2s = np.log2(complement_prob, out=np.zeros_like(complement_prob), where=(complement_prob!=0))

        c_entropy_ngrama = .0
        for c in range(self.n_classes):
            c_entropy_ngrama += complement_prob[c]*complement_log2s[c]
        
        c_entropy_ngrama = (1 - prob_ngrama)*c_entropy_ngrama

        return entropy_ngrama + c_entropy_ngrama

    def gain(self):
        gain_words = {'word':[], 'gain':[]}

        for i, word in enumerate(self.bag):
            print(f'{i}/{len(self.bag)} WORDS PROCESSED')
            gain_words['word'].append(word)
            gain_words['gain'].append(-self.entropy() + self.entropy_ngrama(word))

        
        return pd.DataFrame(gain_words)

        

            
            

