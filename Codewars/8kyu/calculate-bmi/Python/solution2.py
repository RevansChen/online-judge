# Python - 3.4.3

# BMI量表
table = [
    (0, 18.5, 'Underweight'),
    (18.5, 25, 'Normal'),
    (25, 30, 'Overweight')
]

def bmi(weight, height):
    # 計算BMI
    v = weight / height ** 2
    
    # 根據BMI輸出訊息
    for l, u, msg in table:
        if l < v <= u:
            return msg
    return 'Obese'
