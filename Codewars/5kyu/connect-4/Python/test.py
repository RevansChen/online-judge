# Python - 3.4.3

test.describe("Example tests")

# 動作測試
game = Connect4()
test.it("Should return: Player 1 has a turn")
test.assert_equals(game.play(0), "Player 1 has a turn")
test.it("Should return: Player 2 has a turn")
test.assert_equals(game.play(0), "Player 2 has a turn")

# 玩家一勝利的測試
# . . . . . . .
# . . . . . . .
# 1 . . . . . .
# 1 2 . . . . .
# 1 2 . . . . .
# 1 2 . . . . .
game = Connect4()
test.it("Should return: Player 1 has a turn")
test.assert_equals(game.play(0), "Player 1 has a turn")
test.it("Should return: Player 2 has a turn")
test.assert_equals(game.play(1), "Player 2 has a turn")
test.it("Should return: Player 1 has a turn")
test.assert_equals(game.play(0), "Player 1 has a turn")
test.it("Should return: Player 2 has a turn")
test.assert_equals(game.play(1), "Player 2 has a turn")
test.it("Should return: Player 1 has a turn")
test.assert_equals(game.play(0), "Player 1 has a turn")
test.it("Should return: Player 2 has a turn")
test.assert_equals(game.play(1), "Player 2 has a turn")
test.it("Should return: Player 1 wins!")
test.assert_equals(game.play(0), "Player 1 wins!")

# 某一列全滿時的測試
# . . . . 2 . .
# . . . . 1 . .
# . . . . 2 . .
# . . . . 1 . .
# . . . . 2 . .
# . . . . 1 . .
game = Connect4()
test.it("Should return: Player 1 has a turn")
test.assert_equals(game.play(4), "Player 1 has a turn")
test.it("Should return: Player 2 has a turn")
test.assert_equals(game.play(4), "Player 2 has a turn")
test.it("Should return: Player 1 has a turn")
test.assert_equals(game.play(4), "Player 1 has a turn")
test.it("Should return: Player 2 has a turn")
test.assert_equals(game.play(4), "Player 2 has a turn")
test.it("Should return: Player 1 has a turn")
test.assert_equals(game.play(4), "Player 1 has a turn")
test.it("Should return: Player 2 has a turn")
test.assert_equals(game.play(4), "Player 2 has a turn")
test.it("Should return: Column full!")
test.assert_equals(game.play(4), "Column full!")

# 玩家一勝利的測試 + 分出勝負後再動作的測試
# . . . . . . .
# . . . . . . .
# . . . . . . .
# . . . . . . .
# . 2 2 2 . . .
# . 1 1 1 1 . .
game = Connect4()
test.it("Should return: Player 1 has a turn")
test.assert_equals(game.play(1), "Player 1 has a turn")
test.it("Should return: Player 2 has a turn")
test.assert_equals(game.play(1), "Player 2 has a turn")
test.it("Should return: Player 1 has a turn")
test.assert_equals(game.play(2), "Player 1 has a turn")
test.it("Should return: Player 2 has a turn")
test.assert_equals(game.play(2), "Player 2 has a turn")
test.it("Should return: Player 1 has a turn")
test.assert_equals(game.play(3), "Player 1 has a turn")
test.it("Should return: Player 2 has a turn")
test.assert_equals(game.play(3), "Player 2 has a turn")
test.it("Should return: Player 1 wins!")
test.assert_equals(game.play(4), "Player 1 wins!")
test.it("Should return: Game has finished!")
test.assert_equals(game.play(4), "Game has finished!")
