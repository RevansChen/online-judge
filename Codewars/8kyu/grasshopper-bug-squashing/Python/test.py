# Python - 3.6.0

Test.describe('syntax bug fixes')

Test.it('should define varirables and store values')
Test.assert_equals(health, 100)
Test.assert_equals(position, 0)
Test.assert_equals(coins, 0)

main()

Test.describe('runtime error bug fixes')
Test.it('should roll dice first')
Test.assert_equals(log[0], 'roll_dice')

Test.it('should move second')
Test.assert_equals(log[1], 'move')

Test.it('should combat third')
Test.assert_equals(log[2], 'combat')

Test.it('should get coins fourth')
Test.assert_equals(log[3], 'get_coins')

Test.it('should buy health fifth')
Test.assert_equals(log[4], 'buy_health')

Test.it('should print status sixth')
Test.assert_equals(log[5], 'print_status')
