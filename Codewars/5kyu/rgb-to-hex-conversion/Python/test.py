# Python - 2.7.6

test.assert_equals(rgb(0, 0, 0),'000000', 'testing zero values')
test.assert_equals(rgb(1, 2, 3),'010203', 'testing near zero values')
test.assert_equals(rgb(255, 255, 255), 'FFFFFF', 'testing max values')
test.assert_equals(rgb(254, 253, 252), 'FEFDFC', 'testing near max values')
test.assert_equals(rgb(-20, 275, 125), '00FF7D', 'testing out of range values')
