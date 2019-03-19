# Python - 3.6.0

from math import cos, sin

def testing(f, u, l, n, expected):
    Test.assert_equals(interp(f, u, l, n), expected)

Test.describe('interp')
Test.it('Basic tests x -> x')
testing(lambda x : x, 0, 9.0, 4, [0.0, 2.25, 4.5, 6.75])
testing(lambda x : x, 0, 15.0, 9, [0.0, 1.66, 3.33, 5.0, 6.66, 8.33, 10.0, 11.66, 13.33])

Test.it('Basic tests x -> sin(x)')
testing(lambda x : sin(x), 0, 18.0, 12, [0.0, 0.99, 0.14, -0.98, -0.28, 0.93, 0.41, -0.88, -0.54, 0.8, 0.65, -0.72])
testing(lambda x : sin(x), 0, 21.0, 10, [0.0, 0.86, -0.88, 0.01, 0.85, -0.88, 0.03, 0.84, -0.89, 0.05])

Test.it('Basic tests x -> cos(x)')
testing(lambda x : cos(x), 0, 21.0, 7, [1.0, -0.99, 0.96, -0.92, 0.84, -0.76, 0.66])
testing(lambda x : cos(x), 0, 15.0, 12, [1.0, 0.31, -0.81, -0.83, 0.28, 0.99, 0.34, -0.79, -0.84, 0.25, 0.99, 0.37])
