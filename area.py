# area.py
from tools.draw import *
from tools.count import *


def area(area_lis, out_path):
    area_dic = count(area_lis)
    draw_map(area_dic, out_path, '地域分布')
