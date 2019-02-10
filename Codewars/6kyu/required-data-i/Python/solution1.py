# Python - 3.6.0

def count_sel(lst):
    dic = {num: lst.count(num) for num in set(lst)}

    maxCount = max(dic.values())
    sCount = len([num for num, cnt in dic.items() if cnt == 1])
    ls = [num for num, cnt in dic.items() if cnt == maxCount]
    return [len(lst), len(dic), sCount, [sorted(ls), maxCount]]
