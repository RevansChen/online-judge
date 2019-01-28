# Python - 3.6.0

def rps(p1, p2):
    lst = ['scissors', 'paper', 'rock']
    i1, i2 = lst.index(p1), lst.index(p2)
    return ['Draw!', 'Player 2 won!', 'Player 1 won!'][i1 - i2 + (0 if i1 >= i2 else 3)]
