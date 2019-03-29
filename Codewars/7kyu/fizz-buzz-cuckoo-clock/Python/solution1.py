# Python - 3.6.0

def fizz_buzz_cuckoo_clock(time):
    h, m = [*map(int, time.split(':'))]
    h %= 12
    if h == 0:
        h = 12
    
    if (m == 0) or (m == 30):
        return ' '.join(['Cuckoo'] * (1 if m else h))
    elif (m % 15) == 0:
        return 'Fizz Buzz'
    elif (m % 3) == 0:
        return 'Fizz'
    elif (m % 5) == 0:
        return 'Buzz'
        
    return 'tick'
