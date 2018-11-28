# Python - 2.7.6

def find_next_square(sq):
    num = int(sq ** 0.5)
    return (num + 1) ** 2 if (num ** 2) == sq else -1
