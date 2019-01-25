# Python - 3.6.0

Test.describe('Basic tests')
Test.assert_equals(remove_exclamation_marks('Hello World!'), 'Hello World')
Test.assert_equals(remove_exclamation_marks('Hello World!!!'), 'Hello World')
Test.assert_equals(remove_exclamation_marks('Hi! Hello!'), 'Hi Hello')
Test.assert_equals(remove_exclamation_marks(''), '')
Test.assert_equals(remove_exclamation_marks('Oh, no!!!'), 'Oh, no')
