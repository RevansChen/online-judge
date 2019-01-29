# Python - 3.6.0

Test.describe('Sample Tests!')
test.assert_equals(whoseMove('black', False), 'white')
test.assert_equals(whoseMove('white', False), 'black')
test.assert_equals(whoseMove('black', True), 'black')
test.assert_equals(whoseMove('white', True), 'white')
