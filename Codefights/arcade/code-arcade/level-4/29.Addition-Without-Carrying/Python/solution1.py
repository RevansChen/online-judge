# Python3

def additionWithoutCarrying(param1, param2):
    str1, str2 = str(param1), str(param2)
    width = max(len(str(str1)), len(str(str2)))
    num1 = [*map(int, str1.rjust(width, '0'))]
    num2 = [*map(int, str2.rjust(width, '0'))]
    return int(''.join(map(str, [(num1[i] + num2[i]) % 10 for i in range(width)])))
