# sex.py
from tools.count import *
from tools.getdate import *
from tools.draw import *


# 性别分布
def sex(sex_df, out_path):
    # 修改时间格式
    date_lis = getdate(list(sex_df.loc[:, '发布日期']))
    for i in range(len(sex_df)):
        sex_df.loc[i+1, '发布日期'] = date_lis[i]

    # 筛选男、女
    man_df = sex_df.loc[sex_df['性别'] == '男'].loc[:, '发布日期']
    woman_df = sex_df.loc[sex_df['性别'] == '女'].loc[:, '发布日期']

    # 计数
    man_dic = count(man_df)
    woman_dic = count(woman_df)

    # 绘制面积堆积图
    draw_stacked([man_dic, woman_dic], ['男', '女'], out_path, 'sex', '时间', '微博数')


# # 绘制饼图
# def draw_pie(path, dic, png_name):
#     # 解决中文乱码
#     plt.rcParams["font.sans-serif"] = ["SimHei"]
#     plt.rcParams["axes.unicode_minus"] = False
#
#     patches,texts,autotexts = plt.pie(list(dic.values()), labels=list(dic.keys()), autopct='%1.1f%%')
#     for i in range(len(autotexts)):
#         if i == 0:
#             print(texts[i].set_y(0.1))
#             print(autotexts[i].set_y(0.1))
#     plt.savefig(path + png_name + '.png')
#     plt.show()


