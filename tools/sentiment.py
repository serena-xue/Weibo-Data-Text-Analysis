# sentiment.py
from snownlp import SnowNLP
import numpy as np
import pandas as pd


def get_sentiment(fileIn, fileOutPos, fileOutNeg):
    sentimentslist = []
    pos = ['0']
    neg = ['0']
    pos_sentiment = ['sentiment']
    neg_sentiment = ['sentiment']
    
    data = pd.read_csv(fileIn, header=None, encoding='utf-8')
    for i in range(len(data)):
        s = SnowNLP(str(data[0][i]))
        sentiment = s.sentiments
        sentimentslist.append(sentiment)
        if sentiment >= 0.6:
            pos.append(data[0][i])
            pos_sentiment.append(sentiment)
        if sentiment <= 0.4:
            neg.append(data[0][i])
            neg_sentiment.append(sentiment)
    
    dp = [pos, pos_sentiment]
    dp = np.transpose(pd.DataFrame(dp))
    dp = pd.DataFrame(dp).drop(labels=0, axis=0)
    dp.to_csv(fileOutPos, index=False, header=False, encoding='utf-8')

    dn = [neg, neg_sentiment]
    dn = pd.DataFrame(dn)
    dn = pd.DataFrame(np.transpose(dn)).drop(labels=0, axis=0)
    dn.to_csv(fileOutNeg, index=False, header=False, encoding='utf-8')
