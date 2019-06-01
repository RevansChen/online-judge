# Python - 3.6.0

Test.it('should work for some simple example test cases')
test.assert_equals(flatten_and_sort([]), [])
test.assert_equals(flatten_and_sort([[], [1]]), [1])
test.assert_equals(flatten_and_sort([[3, 2, 1], [7, 9, 8], [6, 4, 5]]), [1, 2, 3, 4, 5, 6, 7, 8, 9])
test.assert_equals(flatten_and_sort([[1, 3, 5], [100], [2, 4, 6]]), [1, 2, 3, 4, 5, 6, 100])
