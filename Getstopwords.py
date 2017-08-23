def getstopword(filename):
    stopwords = []
    f = open(filename,'r')
    data = f.readline()
    while data:
        stopwords.append(data)
        data = f.readline()
    return stopwords

if __name__ == 'main':
    stopwords = getstopword('stopwords.txt')
