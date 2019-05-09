# Python - 3.6.0

test.describe('The fusc function -- Part 1')
test.assert_equals(fusc(0), 0)
test.assert_equals(fusc(1), 1)
test.assert_equals([fusc(i) for i in range(21)], [0, 1, 1, 2, 1, 3, 2, 3, 1, 4, 3, 5, 2, 5, 3, 4, 1, 5, 4, 7, 3])
test.assert_equals(fusc(85), 21)

