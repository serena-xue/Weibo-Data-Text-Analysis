# text_analysis.py
from tools.fenci import *
from tools.LDA import *
from tools.sentiment import *
from tools.word_cloud import *

data_path = 'F:/code/python/2022.12/微博数据分析/data/'
out_path = 'F:/code/python/2022.12/微博数据分析/results/'

# 获取微博内容
data = pd.read_csv(data_path + '新能源汽车相关微博数据.csv')
data.loc[1:, '微博内容'].to_csv(data_path + '微博内容.csv', index=False, header=False, encoding='utf-8')

# text_analysis.py
# 情感分析
from tools.sentiment import *
get_sentiment(fileIn=data_path + '微博内容.csv',
              fileOutPos=data_path + 'positive.csv', fileOutNeg=data_path + 'negative.csv')

# text_analysis.py
# 分词
from tools.fenci import *
fenci(fileIn=data_path + '微博内容.csv', fileOut=out_path + '微博内容_分词.csv',
      fileStopWords=data_path + 'stopwords.txt')
fenci(fileIn=data_path + 'positive.csv', fileOut=data_path + 'positive_分词.csv',
      fileStopWords=data_path + 'stopwords.txt')
fenci(fileIn=data_path + 'negative.csv', fileOut=data_path + 'negative_分词.csv',
      fileStopWords=data_path + 'stopwords.txt')

# text_analysis.py
# 提取关键词
get_tags(data_path + '微博内容_分词.csv', out_path + '关键词.txt')
get_tags(data_path + 'positive_分词.csv', out_path + 'positive_关键词.txt')
get_tags(data_path + 'negative_分词.csv', out_path + 'negative_关键词.txt')

# text_analysis.py
# LDA主题模型
from tools.LDA import *
LDA(data_path + '微博内容_分词.csv', out_path + 'LDA.txt')
LDA(data_path + 'positive_分词.csv', out_path + 'positive_LDA.txt')
LDA(data_path + 'negative_分词.csv', out_path + 'negative_LDA.txt')

# text_analysis.py
# 词云
from tools.word_cloud import *
word_cloud(path=out_path, fileIn=data_path + '微博内容_分词.csv',
           figName='词云', png_name='wordcloud')
word_cloud(path=out_path, fileIn=data_path + 'positive_分词.csv',
           figName='positive_词云', png_name='positive_wordcloud')
word_cloud(path=out_path, fileIn=data_path + 'negative_分词.csv',
           figName='negative_词云', png_name='negative_wordcloud')
