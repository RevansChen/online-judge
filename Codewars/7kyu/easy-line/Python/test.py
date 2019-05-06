# Python - 3.6.0

def testing(actual, expected):
    Test.assert_equals(actual, expected)

Test.describe('easyline')
Test.it('Basic tests')
testing(easyline(7), 3432)
testing(easyline(13), 10400600)
testing(easyline(17), 2333606220)
testing(easyline(19), 35345263800)
