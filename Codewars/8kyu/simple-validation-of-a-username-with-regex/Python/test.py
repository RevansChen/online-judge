# Python - 3.6.0

Test.assert_equals(validate_usr('asddsa'), True)
Test.assert_equals(validate_usr('a'), False)
Test.assert_equals(validate_usr('Hass'), False)
Test.assert_equals(validate_usr('Hasd_12assssssasasasasasaasasasasas'), False)
Test.assert_equals(validate_usr(''), False)
Test.assert_equals(validate_usr('____'), True)
Test.assert_equals(validate_usr('012'), False)
Test.assert_equals(validate_usr('p1pp1'), True)
Test.assert_equals(validate_usr('asd43 34'), False)
Test.assert_equals(validate_usr('asd43_34'), True)
