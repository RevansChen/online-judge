# Python - 3.4.3

def stairs_in_20(stairs):
    # 計算出一年走過的階梯數再乘上20
    return sum(sum(stair) for stair in stairs) * 20
