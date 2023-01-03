# count.py
def count(lis):
    # 计数，保存到字典
    num_count = dict()
    for item in lis:
        if item in num_count:
            num_count[item] += 1
        else:
            num_count[item] = 1
    return num_count
