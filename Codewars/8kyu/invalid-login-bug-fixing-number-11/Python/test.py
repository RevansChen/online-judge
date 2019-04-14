# Python - 2.7.6

Test.assert_equals(validate('Timmy', 'password'), 'Successfully Logged in!', 'Should succefully login!')
Test.assert_equals(validate('Timmy', 'h4x0r'), 'Wrong username or password!', 'The password was wrong')
Test.assert_equals(validate('Alice', 'alice'), 'Successfully Logged in!', 'Should succefully login!')
Test.assert_equals(validate('Timmy', 'password"||""=="'), 'Wrong username or password!', 'Should fail to login because of injected code')
Test.assert_equals(validate('Admin', 'gs5bw"||1==1//'), 'Wrong username or password!', 'Should fail to login because of injected code')
