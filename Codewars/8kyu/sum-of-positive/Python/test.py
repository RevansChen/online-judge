# Python - 2.7.6

Test.describe('positive_sum')

Test.it('works for some examples')
Test.assert_equals(positive_sum([1, 2, 3, 4, 5]), 15)
Test.assert_equals(positive_sum([1, -2, 3, 4, 5]), 13)
Test.assert_equals(positive_sum([-1, 2, 3, 4, -5]), 9)

Test.it('returns 0 when array is empty')
Test.assert_equals(positive_sum([]), 0)

Test.it('returns 0 when all elements are negative')
Test.assert_equals(positive_sum([-1, -2, -3, -4, -5]), 0)
