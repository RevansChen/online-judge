# Python - 3.6.0

Test.describe('printer_error')
Test.it('Basic tests')
s = 'aaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyz'
Test.assert_equals(printer_error(s), '3/56')
