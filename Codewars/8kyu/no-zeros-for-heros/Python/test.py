# Python - 3.6.0

def testing(actual, expected):
    Test.assert_equals(actual, expected)

Test.describe('common_left_edge')
Test.it('Basic tests')
testing(no_boring_zeros(1450), 145)
testing(no_boring_zeros(960000), 96)
testing(no_boring_zeros(1050), 105)
testing(no_boring_zeros(-1050), -105)
testing(no_boring_zeros(0), 0)
