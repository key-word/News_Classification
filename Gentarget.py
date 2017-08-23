import numpy

def _gentarget_6news(filename):
    f = open(filename,'r')
    line = f.readline()
    targetTrain = []
    while line:
        words = line.split()
        if words[0] == 'Auto':
            targetTrain.append(1)
        elif words[0] == 'Culture':
            targetTrain.append(2)
        elif words[0] == 'Economy':
            targetTrain.append(3)
        elif words[0] == 'Medicine':
            targetTrain.append(4)
        elif words[0] == 'Military':
            targetTrain.append(5)
        elif words[0] == 'Sports':
            targetTrain.append(6)
        else:
            print 'wrong line: '+line
        line = f.readline()

    f.close()
    return targetTrain


def _fetch_6news_data(filename):
    f = open(filename, 'r')
    line = f.readline()
    news_data = []
    while line:
        news_data.append(line)
        line = f.readline()
    return news_data


def fetch_6news(ori_file,splits_file):
    class News():
        def __init__(self):
            self.data = []
            self.target = []

    target = _gentarget_6news(ori_file)
    data = _fetch_6news_data(splits_file)
    news = News()
    news.data = numpy.array(data)
    news.target = target
    return news


if __name__ == 'main':
    targetTrain = fetch_6news('trainT.txt','trainTwords.txt')
