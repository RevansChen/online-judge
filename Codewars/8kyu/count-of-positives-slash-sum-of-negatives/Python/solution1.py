# Python - 3.4.3

def count_positives_sum_negatives(arr):
    # 輸入為空陣列則傳回空陣列
    if len(arr) == 0:
        return []
    
    count, sum = 0, 0
    for e in arr:
        if e > 0:
            # 統計正整數數量
            count += 1
        else:
            # 累加負整數
            sum += e

    return [count, sum]