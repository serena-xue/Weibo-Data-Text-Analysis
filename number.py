# number.py
from tools.count import *
from tools.getdate import *
from tools.draw import *


# 数量变化
def number(date_lis, out_path):
    # 获取日期格式：年份/月份
    lis_mon = getdate(date_lis)

    # 绘图
    time_dic = count(lis_mon)
    draw_line(out_path, dic_lis=[time_dic], png_name='time',
              xlabel='时间', ylabel='微博数')

