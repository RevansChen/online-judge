# Python - 3.6.0

test.describe('Example Tests')

tests = [
    (0, 1),
    (1, 1),
    (2, 2),
    (3, 6),
    (4, 24),
    (5, 120),
    (6, 720),
    (7, 5040)
]

for inp, exp in tests:
    test.assert_equals(factorial(inp), exp)
