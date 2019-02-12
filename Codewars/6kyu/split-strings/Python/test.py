# Python - 3.6.0

test.describe('Example Tests')

tests = [
    ('asdfadsf', ['as', 'df', 'ad', 'sf']),
    ('asdfads', ['as', 'df', 'ad', 's_']),
    ('', []),
    ('x', ['x_'])
]

for inp, exp in tests:
    test.assert_equals(solution(inp), exp)
