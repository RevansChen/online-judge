# Python - 3.6.0

def is_triangle_number(number):
    if type(number) != int:
        return False

    n, d = 0, 1
    while n < number:
        n += d
        d += 1

    return (number == n) or (number == 0)
