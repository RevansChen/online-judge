# Python - 3.6.0

get_grade = lambda *scores: [*filter(lambda t: t[0](sum(scores) / len(scores)), [
    (lambda n: 90 <= n <= 100, 'A'),
    (lambda n: 80 <= n <  90,  'B'),
    (lambda n: 70 <= n <  80,  'C'),
    (lambda n: 60 <= n <  70,  'D'),
    (lambda n: 0  <= n <  60,  'F')
])][0][1]

