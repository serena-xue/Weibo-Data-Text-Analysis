from number import *
from sex import *
from area import *
from emotion import *
from hot import *

out_path = 'F:/code/python/2022.12/微博数据分析/results/'
data = pd.read_csv('F:/code/python/2022.12/微博数据分析/data/新能源汽车相关微博数据.csv')

# 数量-时间折线图
from number import *
number(list(data.loc[1:, '发布日期']), out_path)

# main.py
# 性别分布变化图
from sex import *
sex(data.loc[1:, ['性别', '发布日期']], out_path)

# main.py
# 地域分布
from area import *
area(list(data.loc[1:, '地域']), out_path)

# main.py
# 微博情绪随时间变化图
from emotion import *
emotion(data.loc[1:, ['微博情绪', '发布日期']], out_path)

# main.py
# 热点微博
from hot import *
hot(data.loc[1:], out_path)
