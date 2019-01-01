# Python - 3.6.0

Test.describe('Basic tests')
Test.it('Fixed Min')
Test.assert_equals(min([-52, 56, 30, 29, -54, 0, -110]), -110)
Test.assert_equals(min([42, 54, 65, 87, 0]), 0)
Test.assert_equals(min([1, 2, 3, 4, 5, 10]), 1)
Test.assert_equals(min([-1, -2, -3, -4, -5, -10]), -10)
Test.assert_equals(min([9]), 9)

Test.it('Fixed Max')
Test.assert_equals(max([-52, 56, 30, 29, -54, 0, -110]), 56)
Test.assert_equals(max([4, 6, 2, 1, 9, 63, -134, 566]), 566)
Test.assert_equals(max([5]), 5)
Test.assert_equals(max([534, 43, 2, 1, 3, 4, 5, 5, 443, 443, 555, 555]), 555)
Test.assert_equals(max([9]), 9)
