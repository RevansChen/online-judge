# CoffeeScript - 1.10.0

describe 'Testing multiply', ->
    it 'Should return a result', ->
        Test.assertEquals multiply(0, 1), 0
        Test.assertEquals multiply(1, 1), 1
        Test.assertEquals multiply(2, 2), 4
        Test.assertEquals multiply(3, 3), 9
        Test.assertEquals multiply(4, 3), 12
        Test.assertEquals multiply(5, 3), 15
        Test.assertEquals multiply(10, 8), 80
        Test.assertEquals multiply(10, 10), 100
        Test.assertEquals multiply(10, -10), -100
        Test.assertEquals multiply(-10, 10), -100
        Test.assertEquals multiply(-10, -10), 100
        Test.assertEquals multiply(20, 10), 200