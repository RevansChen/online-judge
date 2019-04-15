# Python - 3.6.0

grader = lambda score: [*filter(lambda t: t[0](score), [
    (lambda n: n > 1.0 or n < 0.6, 'F'),
    (lambda n: 0.9 <= n <= 1.0, 'A'),
    (lambda n: 0.8 <= n <  0.9, 'B'),
    (lambda n: 0.7 <= n <  0.8, 'C'),
    (lambda n: 0.6 <= n <  0.7, 'D')
])][0][1]

