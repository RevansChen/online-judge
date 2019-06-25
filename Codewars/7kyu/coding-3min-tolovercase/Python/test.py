# Python - 3.6.0

Test.describe('Basic Tests')
Test.assert_equals(to_lover_case('LOVE'), 'EVOL')
Test.assert_equals(to_lover_case('love'), 'EVOL')
Test.assert_equals(to_lover_case('abcd'), 'LOVE')
Test.assert_equals(to_lover_case('ebcd'), 'LOVE')
Test.assert_equals(to_lover_case('Hello World!'), 'ELEEV VVOEE!')
Test.assert_equals(to_lover_case('jrvz,'), 'OOOO,')
