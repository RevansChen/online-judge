# Python - 3.6.0

BASIC_TESTS = (
    (('45', '1'), '1451'),
    (('13', '200'), '1320013'),
    (('Soon', 'Me'), 'MeSoonMe'),
    (('U', 'False'), 'UFalseU')
)

test.describe('Basic Tests')
for pair, result in BASIC_TESTS:
    test.it("'{}', '{}'".format(*pair))
    test.assert_equals(solution(*pair), result)
