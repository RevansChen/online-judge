# Python - 3.6.0

test.describe('Example Tests')

tests = [
    # [input, expected],
    ['ablak', 'ablaknak'],
    ['tükör', 'tükörnek'],
    ['keret', 'keretnek'],
    ['otthon', 'otthonnak'],
    ['virág', 'virágnak'],
    ['tett', 'tettnek'],
    ['rokkant', 'rokkantnak'],
    ['rossz', 'rossznak']
]

for inp, exp in tests:
    result = dative(inp)
    print(f'input: {inp}\nexpected: {exp}\nyour result: {result}')
    test.assert_equals(result, exp)
