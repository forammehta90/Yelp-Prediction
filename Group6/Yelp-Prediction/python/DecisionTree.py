
import sys
import json
import csv
import numpy as np
import pandas as pd
from pandas.io.json import json_normalize
from collections import Counter
from sklearn.base import TransformerMixin
from scipy.sparse import *


class DecisionTree(object):
    def __init__(self,testList):
        self.testList = testList
        self.labels = []
    def loadFiles(self):
        
        dataset = list()
        dataset_test = list()
        file = '/Users/forammehta/Desktop/foram/sjsu/255/Project/Yelp-Prediction/files/business_binary_le_finally_train.csv'
        with open(file, 'r') as f:
            reader = csv.reader(f)
            your_list = list(reader)

        for l in your_list:
            dataset.append(l[0:-1])
            self.labels.append(l[-1])

        return self.csr(dataset)

    def csr(self,dataset):
        docs = list()
        for list2 in dataset:
            docs.append([int(n) if n != '' else 0 for n in list2])
        dataset_csr_train = csr_matrix(docs)

        docs_test = list()
        docs_test.append([int(n) if n != '' else 0 for n in self.testList])
        dataset_csr_test = csr_matrix(docs_test)

        return self.normalize(dataset_csr_train,dataset_csr_test)
        
    def normalize(self,dataset_csr_train,dataset_csr_test):
        from sklearn import preprocessing
        mat_train = preprocessing.normalize(dataset_csr_train, norm='l2')
        mat_test = preprocessing.normalize(dataset_csr_test, norm='l2')
        return self.DR(mat_train,mat_test)

    def DR(self,mat_train,mat_test):
        from sklearn.model_selection import cross_val_score
        from sklearn.neural_network import MLPClassifier
        from sklearn.feature_selection import SelectKBest
        from sklearn.feature_selection import chi2

        ch2_model = SelectKBest(chi2, k='all').fit(mat_train, self.labels)
        X_chi2 = ch2_model.transform(mat_train)
        X_chi2_test = ch2_model.transform(mat_test)
        return self.dtree_classify(X_chi2,X_chi2_test)

    def dtree_classify(self,X_chi2,X_chi2_test):
        from sklearn.metrics import f1_score
        from sklearn import tree
        
        clf = tree.DecisionTreeClassifier()
        y_predict = clf.fit(X_chi2.todense(), self.labels).predict(X_chi2_test.todense())

        return y_predict
