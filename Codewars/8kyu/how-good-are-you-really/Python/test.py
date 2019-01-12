# Python - 3.6.0

test.describe('Basic Tests')

test.it('better_than_average([2, 3], 5) should return True')
test.assert_equals(better_than_average([2, 3], 5), True)

test.it('better_than_average([100, 40, 34, 57, 29, 72, 57, 88], 75) should return True')
test.assert_equals(better_than_average([100, 40, 34, 57, 29, 72, 57, 88], 75), True)

test.it('better_than_average([12, 23, 34, 45, 56, 67, 78, 89, 90], 69) should return True')
test.assert_equals(better_than_average([12, 23, 34, 45, 56, 67, 78, 89, 90], 69), True)
