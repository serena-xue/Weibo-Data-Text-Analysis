# emotion.py
from tools.count import *
from tools.draw import *
from tools.getdate import *


def emotion(emo_df, out_path):
    # 修改时间格式
    date_lis = getdate(list(emo_df.loc[:, '发布日期']))
    for i in range(len(emo_df)):
        emo_df.loc[i+1, '发布日期'] = date_lis[i]

    # 筛选男、女
    xi_yue_df = emo_df.loc[emo_df['微博情绪'] == '喜悦'].loc[:, '发布日期']
    kong_ju_df = emo_df.loc[emo_df['微博情绪'] == '恐惧'].loc[:, '发布日期']
    zhong_xing_df = emo_df.loc[emo_df['微博情绪'] == '中性'].loc[:, '发布日期']
    fen_nu_df = emo_df.loc[emo_df['微博情绪'] == '愤怒'].loc[:, '发布日期']
    bei_shang_df = emo_df.loc[emo_df['微博情绪'] == '悲伤'].loc[:, '发布日期']
    jing_qi_df = emo_df.loc[emo_df['微博情绪'] == '惊奇'].loc[:, '发布日期']

    # 计数
    xi_yue_dic = count(xi_yue_df)
    kong_ju_dic = count(kong_ju_df)
    zhong_xing_dic = count(zhong_xing_df)
    fen_nu_dic = count(fen_nu_df)
    bei_shang_dic = count(bei_shang_df)
    jing_qi_dic = count(jing_qi_df)

    draw_stacked(dic_lis=[xi_yue_dic, kong_ju_dic, zhong_xing_dic, fen_nu_dic, bei_shang_dic, jing_qi_dic],
                 labels=['喜悦', '恐惧', '中性', '愤怒', '悲伤', '惊奇'], path=out_path,
                 xlabel='时间', ylabel='数量', png_name='emotion')
    draw_stacked([xi_yue_dic, kong_ju_dic, fen_nu_dic, bei_shang_dic, jing_qi_dic],
                 labels=['喜悦', '恐惧', '愤怒', '悲伤', '惊奇'], path=out_path,
                 xlabel='时间', ylabel='数量', png_name='emotion2')
