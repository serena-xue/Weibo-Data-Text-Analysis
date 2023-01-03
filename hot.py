# hot.py
def hot(hot_df, out_path):
    hot_df['sum'] = hot_df['转'] + hot_df['评'] + hot_df['赞']
    hot_df_sorted = hot_df.sort_values('sum', ascending=False)
    hot_df_sorted.iloc[:4].to_csv(out_path + 'hot.csv', index=None)
