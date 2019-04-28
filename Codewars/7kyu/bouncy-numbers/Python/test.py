# Python - 3.6.0

Test.describe('Sample Test Cases')

Test.it('Small Numbers')
Test.assert_equals(is_bouncy(0), False)
Test.assert_equals(is_bouncy(99), False)
Test.assert_equals(is_bouncy(101), True)
Test.assert_equals(is_bouncy(120), True)
Test.assert_equals(is_bouncy(122), False)
Test.assert_equals(is_bouncy(221), False)
