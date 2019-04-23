# Python - 2.7.6

sexy_name = lambda name: filter(lambda t: t[0](sum(map(lambda c: {
    'A': 100, 'B': 14,  'C': 9,   'D': 28,  'E': 145, 'F': 12,  'G': 3,
    'H': 10,  'I': 200, 'J': 100, 'K': 114, 'L': 100, 'M': 25,
    'N': 450, 'O': 80,  'P': 2,   'Q': 12,  'R': 400, 'S': 113, 'T': 405,
    'U': 11,  'V': 10,  'W': 10,  'X': 3,   'Y': 210, 'Z': 23
}.get(c, 0), name.upper()))), [
    (lambda n:       n <= 60,  'NOT TOO SEXY'),
    (lambda n: 60  < n <= 300, 'PRETTY SEXY'),
    (lambda n: 300 < n <  600, 'VERY SEXY'),
    (lambda n:       n >= 600, 'THE ULTIMATE SEXIEST')
])[0][1]
