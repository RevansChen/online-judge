# Python - 3.4.3

test.describe('Example Tests')
InterlacedSpiralCipher = {'encode': encode, 'decode': decode }

example1A = 'Romani ite domum'
example1B = 'Rntodomiimuea  m'
test.assert_equals(InterlacedSpiralCipher['encode'](example1A), example1B)
test.assert_equals(InterlacedSpiralCipher['decode'](example1B), example1A)

example2A = 'Sic transit gloria mundi'
example2B = 'Stsgiriuar i ninmd l otac'
test.assert_equals(InterlacedSpiralCipher['encode'](example2A), example2B)
test.assert_equals(InterlacedSpiralCipher['decode'](example2B), example2A)
