from pyltp import Segmentor
segmentor = Segmentor()
segmentor.load('/usr/local/ltp_data_v3.4.0/cws.model')
trainT = open('trainT.txt','r+')
trainTwords = open('trainTwords.txt','w+')
line = trainT.readline()

while line:
    line = line.replace('\n', '')
    line = line.replace('\r', '')
    line = line.replace(' ', '')
    words = segmentor.segment(line)
    trainTwords.write(' '.join(words)+'\n')
    line = trainT.readline()

trainT.close()
trainTwords.close()
