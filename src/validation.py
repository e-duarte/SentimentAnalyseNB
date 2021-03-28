from sklearn.model_selection import cross_validate
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.metrics import make_scorer
import numpy as np


def confusion_matrix_scorer(clf, X, y):
      y_pred = clf.predict(X)
      cm = confusion_matrix(y, y_pred)
      return {'tn': cm[0, 0], 'fp': cm[0, 1],
              'fn': cm[1, 0], 'tp': cm[1, 1]}


def k_cross_validate(clf, X, y, k):
    cv_results = cross_validate(
        clf, X, y, cv=k,
        scoring=confusion_matrix_scorer
    )
    tp = int(cv_results['test_tp'].mean())
    fp = int(cv_results['test_fp'].mean())
    fn = int(cv_results['test_fn'].mean())
    tn = int(cv_results['test_tn'].mean())
    return {
        'tp': tp, 'fp': fp,
        'fn':fn, 'tn': tn,
        'accuracy': (tp+tn)/(tp+fn+fp+tn),
        'precision': tp/(tp+fp),
        'cm': np.array([[tp, fp], [fn, tn]])
    }

def hold_out(X, y):
    #Hold out validation
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=0, shuffle=True
    )
    gnb = GaussianNB()
    gnb.fit(X_train, y_train)
    y_pred = cnb.predict(X_test)
    print("Number of mislabeled points out of a total %d points : %d"
       % (X_test.shape[0], (y_test != y_pred).sum()))