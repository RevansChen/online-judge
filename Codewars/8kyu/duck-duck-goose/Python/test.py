# Python - 3.6.0

test.describe('fixed tests')
test.it('should find the correct goose')
test.assert_equals(duck_duck_goose(players, 1),  'a')
test.assert_equals(duck_duck_goose(players, 3),  'c')
test.assert_equals(duck_duck_goose(players, 10), 'z')
test.assert_equals(duck_duck_goose(players, 20), 'z')
test.assert_equals(duck_duck_goose(players, 30), 'z')
test.assert_equals(duck_duck_goose(players, 18), 'g')
test.assert_equals(duck_duck_goose(players, 28), 'g')
test.assert_equals(duck_duck_goose(players, 12), 'b')
test.assert_equals(duck_duck_goose(players, 2),  'b')
test.assert_equals(duck_duck_goose(players, 7),  'f')
