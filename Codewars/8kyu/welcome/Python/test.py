# Python - 3.6.0

Test.describe('Basic tests')
Test.assert_equals(greet('english'), 'Welcome')
Test.assert_equals(greet('dutch'), 'Welkom')
Test.assert_equals(greet('IP_ADDRESS_INVALID'), 'Welcome')
Test.assert_equals(greet(''), 'Welcome')
Test.assert_equals(greet(2), 'Welcome')
