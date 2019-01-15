# Python - 2.7.6

test.describe('Fixed Tests')
test.it('Tests')
test.assert_equals(pipe_fix([1, 2, 3, 5, 6, 8, 9]), [1, 2, 3, 4, 5, 6, 7, 8, 9])
test.assert_equals(pipe_fix([1, 2, 3, 12]), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
test.assert_equals(pipe_fix([6, 9]), [6, 7, 8, 9])
test.assert_equals(pipe_fix([-1, 4]), [-1, 0, 1, 2, 3, 4])
test.assert_equals(pipe_fix([1, 2, 3]), [1, 2, 3])
