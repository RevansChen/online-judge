# Python - 3.4.3

def fuel_price(litres, pricePerLiter):
    # 計算每公升油價的折扣, 折扣最多0.25元
    discount = min((litres // 2) * 0.05, 0.25)
    
    # 計算總油價, 並四捨五入至小數第二位
    return round((pricePerLiter - discount) * litres, 2)
