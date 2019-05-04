# Python - 3.6.0

test.describe('Basic tests')

test.assert_equals(hex_word_sum('DEFACE'), 14613198, 'Should convert hex to decimal correctly')
test.assert_equals(hex_word_sum('SAFE'), 23294, 'Should be able to interpret "S" as "5"')
test.assert_equals(hex_word_sum('CODE'), 49374, 'Should be able to interpret "O" as "0"')
test.assert_equals(hex_word_sum('BUGS'), 0, 'A word that cannot be converted to hex has value of 0')
test.assert_equals(hex_word_sum(''), 0, 'Empty string returns 0')
test.assert_equals(hex_word_sum('DO YOU SEE THAT BEE DRINKING DECAF COFFEE'), 13565769, 'Should work with multiple words')
test.assert_equals(hex_word_sum('ASSESS ANY BAD CODE AND TRY AGAIN'), 10889952, 'Should work with multiple words')
