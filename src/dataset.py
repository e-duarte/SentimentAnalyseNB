import pandas as pd
import re

class Dataset:
    def __init__(self, X, Y):
        self.dataset = pd.concat([X,Y], axis=1)

        self.pat = '^({} )| {} |( {})$|{}'

    def find_x_column(self, x, column):
        x = f'\{x}' if x == '?' else x

        indexs = []
        for i, e in enumerate(self.dataset[column]):
            if re.search(self.pat.format(x, x, x, x), e):
                indexs.append(i)

        return self.dataset.iloc[indexs]
    
    def find_x_y_column(self, x, y, column_x, column_y):
        y = f'\{y}' if y == '?' else y
        reduzed_dt = self.find_x_column(x, column_x)

        indexs = []
        for i, e in enumerate(reduzed_dt[column_y]):
            if re.search(self.pat.format(y, y, y, y), e):
                indexs.append(i)
        
        return self.dataset.iloc[indexs]
    
    def find_x_neg_column(self, x, column):
        return self.dataset.drop(self.find_x_column(x, column).index)
    
    def find_x_y_neg_column(self, x, y, column_x, column_y):
        y = f'\{y}' if y == '?' else y
        reduzed_dt = self.find_x_neg_column(x, column_x)

        indexs = []
        for i, e in enumerate(reduzed_dt[column_y]):
            if re.search(self.pat.format(y, y, y, y), e):
                indexs.append(i)
        
        return self.dataset.iloc[indexs]

    
    
