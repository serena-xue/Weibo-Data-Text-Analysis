from pyecharts.charts import Map
from pyecharts.options import *
import matplotlib.pyplot as plt


# 折线图
def draw_line(path, dic_lis, xlabel, ylabel, png_name):
    # 解决中文乱码
    plt.rcParams["font.sans-serif"] = ["SimHei"]
    plt.rcParams["axes.unicode_minus"] = False

    # 绘制折线图：dic.keys()作为横轴，dic.values()作为纵轴
    fig = plt.figure(dpi=128, figsize=(10, 6))
    for i in range(len(dic_lis)):
        dic = dic_lis[i]
        plt.plot(list(dic.keys()), list(dic.values()), '-o', color='#80B1D3')

    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    fig.autofmt_xdate()  # 横轴标签斜着显示

    plt.savefig(path + png_name + '.png')
    plt.show()


# draw.py
# 堆积面积图
def draw_stacked(dic_lis, labels, path, png_name, xlabel, ylabel):
    color_lis = ['#80B1D3', '#FB8072', '#7FC97F', '#E377C2', '#7F7F7F', '#17BECF']

    # 解决中文乱码
    plt.rcParams["font.sans-serif"] = ["SimHei"]
    plt.rcParams["axes.unicode_minus"] = False

    fig = plt.figure(dpi=128, figsize=(10, 6))

    # 整理数据
    x = list(dic_lis[0].keys())  # 横坐标
    y = []
    for i in range(len(dic_lis)):
        y.append(list(dic_lis[i].values()))  # 6*11的列表

    # 绘图
    ax = plt.gca()
    ax.stackplot(x, y, labels=labels, colors=color_lis, alpha=0.8)

    plt.legend(fontsize=10, ncol=4)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    fig.autofmt_xdate()  # 横轴标签斜着显示

    plt.savefig(path + png_name + '.png')
    plt.show()


# draw.py
# 地理图
def draw_map(data, out_file_name):
    # 整理数据
    data.pop('其他')
    data.pop('海外')
    key_lis = list(data.keys()).copy()
    for key in key_lis:
        if key == '上海' or key == '北京' or key == '重庆' or key == '天津':
            data[key + '市'] = data.pop(key)
        elif key == '新疆':
            data[key + '维吾尔自治区'] = data.pop(key)
        elif key == '内蒙古':
            data[key + '自治区'] = data.pop(key)
        elif key == '香港':
            data[key + '特别行政区'] = data.pop(key)
        elif key == '宁夏':
            data[key + '回族自治区'] = data.pop(key)
        else:
            data[key + '省'] = data.pop(key)

    # 将字典转换成元组的列表
    items = data.items()
    data_lis = list(items)

    # 准备地图对象
    map = Map()

    # 修饰
    map.set_global_opts(
        title_opts=TitleOpts(title='微博数地域分布'),
        visualmap_opts=VisualMapOpts(
            is_show=True,  # 是否显示
            is_piecewise=True,  # 是否分段
            pieces=[
                {"min": 1, "max": 9, "label": "1~9人", "color": "#CCFFFF"},
                {"min": 10, "max": 99, "label": "10~99人", "color": "#FFFF99"},
                {"min": 100, "max": 999, "label": "100~999人", "color": "#FF9966"},
                {"min": 1000, "max": 3999, "label": "1000~3999人", "color": "#FF6666"},
                {"min": 4000, "label": "4000以上", "color": "#990033"}
            ]  # 分段信息
        )
    )

    # 添加数据
    map.add("微博数地域分布", data_lis, "china")

    # 生成可交互的html地理图
    map.render(out_file_name + '.html')
