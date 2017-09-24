# Python - 3.4.3

def bmi(weight, height):
    # 計算BMI
    v = weight / height ** 2
    
    # 根據BMI輸出訊息
    if v <= 18.5:
        return 'Underweight'
    elif v <= 25:
        return 'Normal'
    elif v <= 30:
        return 'Overweight'
    else:
        return 'Obese'
    