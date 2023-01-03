import pandas as pd

dataAll = pd.read_csv('F:/code/python/2022.12/微博数据分析/data/原微博样本.csv', index_col=0)

# 创建空dataframe
dataCar = pd.DataFrame(data=None, columns=['微博内容', '信息属性', '发布日期',
                       '认证类型', '地域', '城市', '性别', '粉丝数', '微博数',
                       '转', '评', '赞', '话题', '微博情绪', 'MD5-作者ID', 'MD5-mid'])

# 筛选条件：新能源 AND 车
for i in range(len(dataAll['微博内容'])):
    if '新能源' in dataAll.loc[i+1, '微博内容'] and '车' in dataAll.loc[i+1, '微博内容']:
        dataCar = pd.concat([dataCar, pd.DataFrame(dataAll.loc[i+1]).T])

print('原数据条数：', len(dataAll))
print('筛选条件：新能源 AND 车')
print('清洗前数据条数：', len(dataCar))
dataCar = dataCar.drop_duplicates()  # 去重
print('清洗后条数：', len(dataCar))
print('表头：', dataCar.columns)

# 导出csv
dataCar.to_csv('新能源汽车相关微博数据.csv', index=None)
