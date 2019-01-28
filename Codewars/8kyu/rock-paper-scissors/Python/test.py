# Python - 3.6.0

Test.describe('rock paper scissors')
Test.it('player 1 win')
Test.assert_equals(rps('rock', 'scissors'), 'Player 1 won!')
Test.assert_equals(rps('scissors', 'paper'), 'Player 1 won!')
Test.assert_equals(rps('paper', 'rock'), 'Player 1 won!')

Test.it('player 2 win')
Test.assert_equals(rps('scissors', 'rock'), 'Player 2 won!')
Test.assert_equals(rps('paper', 'scissors'), 'Player 2 won!')
Test.assert_equals(rps('rock', 'paper'), 'Player 2 won!')

Test.it('draw')
Test.assert_equals(rps('rock', 'rock'), 'Draw!')
Test.assert_equals(rps('scissors', 'scissors'), 'Draw!')
Test.assert_equals(rps('paper', 'paper'), 'Draw!')
