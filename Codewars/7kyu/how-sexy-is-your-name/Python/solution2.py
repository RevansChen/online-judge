# Python - 2.7.6

sexy_name = lambda name: filter(lambda t: t[0](sum(map(lambda c: SCORES.get(c, 0), name.upper()))), [
    (lambda n:       n <= 60,  'NOT TOO SEXY'),
    (lambda n: 60  < n <= 300, 'PRETTY SEXY'),
    (lambda n: 300 < n <  600, 'VERY SEXY'),
    (lambda n:       n >= 600, 'THE ULTIMATE SEXIEST')
])[0][1]
