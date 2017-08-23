# -*- coding: UTF-8 -*-
from sklearn.feature_extraction.text import HashingVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics
from Gentarget import *
from Getstopwords import *

def calculate_result(actual, pred):
    m_precision = metrics.precision_score(actual,pred, average='weighted')
    m_recall = metrics.recall_score(actual,pred, average='weighted')
    print 'predict info:'
    print 'precision:{0:.3f}'.format(m_precision)
    print 'recall:{0:0.3f}'.format(m_recall)
    print 'f1-score:{0:.3f}'.format(metrics.f1_score(actual,pred, average='weighted'))

news_train = fetch_6news('trainT.txt', 'trainTwords.txt')
news_test = fetch_6news('testT.txt', 'testTwords.txt')

stop_words = getstopword('stopwords.txt')
vectorizer = HashingVectorizer(stop_words= stop_words, non_negative=True, n_features=10000)
fea_train = vectorizer.fit_transform(news_train.data)
fea_test = vectorizer.fit_transform(news_test.data)

clf = MultinomialNB(alpha=0.01)
clf.fit(fea_train,news_train.target)
pred = clf.predict(fea_test)
calculate_result(news_test.target, pred)
