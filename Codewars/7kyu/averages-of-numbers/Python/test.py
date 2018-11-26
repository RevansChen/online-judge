# Python - 3.6.0

test.describe('Example Tests')
tests = (
    ([2, 2, 2, 2], [2, 2, 2, 2, 2]),
    ([0, 0, 0, 0], [2, -2, 2, -2, 2]),
    ([2, 4, 3, -4.5], [1, 3, 5, 1, -10]),
    ([], [])
)

for exp, inp in tests:
    test.assert_equals(averages(inp), exp)
