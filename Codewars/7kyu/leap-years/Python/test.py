# Python - 3.6.0

test.describe('Leap years (should equal True)')
test.assert_equals(isLeapYear(1984), True, 'Year 1984 was a leap year!')
test.assert_equals(isLeapYear(2000), True, 'Year 2000 was a leap year!')

test.describe('Normal years (should equal False)')
test.assert_equals(isLeapYear(1234), False, 'Year 1234 was NOT a leap year!')
test.assert_equals(isLeapYear(1100), False, 'Year 1100 was NOT a leap year!')
