# Python - 3.6.0

Test.describe('Basic tests')
Test.assert_equals(who_is_paying('Mexico'), ['Mexico', 'Me'])
Test.assert_equals(who_is_paying('Melania'), ['Melania', 'Me'])
Test.assert_equals(who_is_paying('Melissa'), ['Melissa', 'Me'])
Test.assert_equals(who_is_paying('Me'), ['Me'])
Test.assert_equals(who_is_paying(''), [''])
Test.assert_equals(who_is_paying('I'), ['I'])
