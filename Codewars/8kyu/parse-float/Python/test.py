# Python - 3.6.0

test.describe('Example Tests')

ts = [
    ('1.0', 1.0),
    ('a', None),
    ('234.0234', 234.0234)
]

for t in ts:
    test.assert_equals(parse_float(t[0]), t[1])
