# getdate.py
def getdate(date_lis):
    # 获取日期格式：年份/月份
    lis_mon = []
    for i in range(len(date_lis)):
        lis_mon.append(date_lis[i].split('/')[0] + '/' + date_lis[i].split('/')[1])
    return lis_mon
