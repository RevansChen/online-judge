# Python - 3.6.0

def testing(actual, expected):
    Test.assert_equals(actual, expected)

Test.describe('max_rot')
Test.it('Basic tests')
testing(max_rot(38458215), 85821534)
testing(max_rot(195881031), 988103115)
testing(max_rot(896219342), 962193428)
testing(max_rot(69418307), 94183076)
