# Python - 3.6.0

test.describe('Fixed tests')
test.assert_equals(whatday(1), 'Sunday')
test.assert_equals(whatday(2), 'Monday')
test.assert_equals(whatday(3), 'Tuesday')
test.assert_equals(whatday(8), 'Wrong, please enter a number between 1 and 7')
test.assert_equals(whatday(20), 'Wrong, please enter a number between 1 and 7')
