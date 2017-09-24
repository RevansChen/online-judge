# Python - 2.7.6

Test.assert_equals(toAscii85('easy'), '<~ARTY*~>')
Test.assert_equals(toAscii85('somewhat difficult'), '<~F)Po,GA(E,+Co1uAnbatCif~>')

Test.assert_equals(fromAscii85('<~ARTY*~>'), 'easy')
Test.assert_equals(fromAscii85('<~F)Po,GA(E,+Co1uAnbatCif~>'), 'somewhat difficult')