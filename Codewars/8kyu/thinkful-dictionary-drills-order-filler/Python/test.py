# Python - 3.6.0

stock = {
    'football': 4,
    'boardgame': 10,
    'leggos': 1,
    'doll': 5
}
test.assert_equals(fillable(stock, 'football', 3), True)
test.assert_equals(fillable(stock, 'leggos', 2), False)
test.assert_equals(fillable(stock, 'action figure', 1), False)
