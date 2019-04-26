# Python - 2.7.6

def testing(actual, expected):
    Test.assert_equals(actual, expected)

Test.describe('new_avg')
Test.it('Basic tests')
testing(new_avg([14, 30, 5, 7, 9, 11, 16], 90), 628)
testing(new_avg([14, 30, 5, 7, 9, 11, 15], 92), 645)
test.expect_error('Error expected', lambda: new_avg([14, 30, 5, 7, 9, 11, 15], 2))
