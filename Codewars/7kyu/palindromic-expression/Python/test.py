# Python - 3.6.0

import math
s = palindromic_expression()
Test.assert_equals(s, s[::-1], 'Must be a palindrome')
try:
    f = eval(s[:math.ceil(len(s) / 2)])
    Test.expect(True, 'Was a function')
    total = sum(map(ord, s))
    Test.assert_equals(f(total), total, 'Must give the correct sum')
except:
    Test.expect(False, 'Must be a function with correct parameters')
