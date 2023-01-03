path = 'F:/code/python/2023.01/旅游业微博数据分析/数据/'

import pandas as pd

data = pd.read_csv(path + '上海旅游.csv')

wids = data.loc[:, 'wid']

print(wids)

wids1 = wids.loc[:100]
wids2 = wids.loc[101:200]
wids3 = wids.loc[201:300]
wids4 = wids.loc[301:400]
wids5 = wids.loc[401:]

wids1.to_csv(path + 'wid1.csv', header=None, index=None)
wids2.to_csv(path + 'wid2.csv', header=None, index=None)
wids3.to_csv(path + 'wid3.csv', header=None, index=None)
wids4.to_csv(path + 'wid4.csv', header=None, index=None)
wids5.to_csv(path + 'wid5.csv', header=None, index=None)