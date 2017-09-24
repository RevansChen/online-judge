# Python - 3.4.3

def count_positives_sum_negatives(arr):
    # 輸入為空陣列則傳回空陣列,
    # 若不為空陣列則統計正整數數量, 並累加負整數
    return [] if len(arr) == 0 else [len([e for e in arr if e > 0]), sum([e for e in arr if e < 0])]