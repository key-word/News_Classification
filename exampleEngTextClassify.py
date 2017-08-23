from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import HashingVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics


def calculate_result(actual,pred):
    m_precision = metrics.precision_score(actual,pred, average='weighted')
    m_recall = metrics.recall_score(actual,pred, average='weighted')
    print 'predict info:'
    print 'precision:{0:.3f}'.format(m_precision)
    print 'recall:{0:0.3f}'.format(m_recall)
    print 'f1-score:{0:.3f}'.format(metrics.f1_score(actual,pred, average='weighted'))

categories = ['comp.graphics', 'comp.os.ms-windows.misc',
              'comp.sys.ibm.pc.hardware', 'comp.sys.mac.hardware',
              'comp.windows.x']

newsgroup_train = fetch_20newsgroups(subset='train',categories=categories)
newsgroup_test = fetch_20newsgroups(subset='test',categories=categories)

vectorizer = HashingVectorizer(stop_words='english', non_negative = True, n_features=10000)
fea_train = vectorizer.fit_transform(newsgroup_train.data)
fea_test = vectorizer.fit_transform(newsgroup_test.data)

clf = MultinomialNB(alpha=0.01)
clf.fit(fea_train,newsgroup_train.target)
pred = clf.predict(fea_test)
calculate_result(newsgroup_test.target,pred)
