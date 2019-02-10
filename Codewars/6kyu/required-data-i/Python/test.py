# Python - 3.6.0

test.describe('Example Tests')
test.assert_equals(count_sel([-3, -2, -1, 3, 4, -5, -5, 5, -1, -5]), [10, 7, 5, [[-5], 3]])
test.assert_equals(count_sel([5, -1, 1, -1, -2, 5, 0, -2, -5, 3]), [10, 7, 4, [[-2, -1, 5], 2]])
test.assert_equals(count_sel([-2, 4, 4, -2, -2, -1, 3, 5, -5, 5]), [10, 6, 3, [[-2], 3]])
test.assert_equals(count_sel([4, -5, 1, -5, 2, 4, -1, 4, -1, 1]), [10, 5, 1, [[4], 3]])
test.assert_equals(count_sel([4, 4, 2, -3, 1, 4, 3, 2, 0, -5, 2, -2, -2, -5]), [14, 8, 4, [[2, 4], 3]])
