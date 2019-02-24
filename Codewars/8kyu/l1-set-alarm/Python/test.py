# Python - 3.6.0

Test.describe('set_alarm')

Test.it('returns correct result for all input values')
Test.assert_equals(set_alarm(True, True), False, 'Fails when input is True, True')
Test.assert_equals(set_alarm(False, True), False, 'Fails when input is False, True')
Test.assert_equals(set_alarm(False, False), False, 'Fails when input is False, False')
Test.assert_equals(set_alarm(True, False), True, 'Fails when input is True, False')
