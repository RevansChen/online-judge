# Python - 3.6.0

test.describe('Basic tests')
test.assert_equals(meeting(['X', 'O', 'X']), 1)
test.assert_equals(meeting(['O', 'X', 'X', 'X', 'X']), 0)
test.assert_equals(meeting(['X', 'X', 'O', 'X', 'X']), 2)
test.assert_equals(meeting(['X']), 'None available!')
