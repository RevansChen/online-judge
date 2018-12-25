# Python - 2.7.6

Test.describe('Basic tests')
Test.assert_equals(validate_hello('hello'), True)
Test.assert_equals(validate_hello('ciao bella!'), True)
Test.assert_equals(validate_hello('salut'), True)
Test.assert_equals(validate_hello('hallo, salut'), True)
Test.assert_equals(validate_hello('hombre! Hola!'), True)
Test.assert_equals(validate_hello("Hallo, wie geht's dir?"), True)
Test.assert_equals(validate_hello('AHOJ!'), True)
Test.assert_equals(validate_hello('czesc'), True)
Test.assert_equals(validate_hello('meh'), False)
Test.assert_equals(validate_hello('Ahoj'), True)
