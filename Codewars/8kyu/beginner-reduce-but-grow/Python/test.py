# Python - 3.6.0

test.describe('Example Tests')
tests = [
    [6 , [1, 2, 3]],
    [16, [4, 1, 1, 1, 4]],
    [64, [2, 2, 2, 2, 2, 2]],
]

for exp, inp in tests:
    test.assert_equals(grow(inp), exp)
