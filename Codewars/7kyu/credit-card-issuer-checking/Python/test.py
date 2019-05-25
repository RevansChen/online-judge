# Python - 3.6.0

test.assert_equals(get_issuer(4111111111111111), 'VISA')
test.assert_equals(get_issuer(378282246310005), 'AMEX')
test.assert_equals(get_issuer(9111111111111111), 'Unknown')
