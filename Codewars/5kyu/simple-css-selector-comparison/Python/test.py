# Python - 2.7.6

Test.describe('Do some testing')
Test.assert_equals(compare('body p', 'div'), 'body p')
Test.assert_equals(compare('.class', '#id'), '#id')
Test.assert_equals(compare('div.big', '.small'), 'div.big')
Test.assert_equals(compare('.big', '.small'), '.small')
