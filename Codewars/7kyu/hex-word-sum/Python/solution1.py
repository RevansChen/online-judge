# Python - 3.6.0

def hex_word_sum(string):
    sum = 0
    for h in [s.replace('O', '0').replace('S', '5') for s in string.split(' ')]:
        try:
            sum += int(h, 16)
        except:
            pass
    return sum
