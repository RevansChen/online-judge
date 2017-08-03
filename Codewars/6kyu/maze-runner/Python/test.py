test.describe("Example tests")

# 迷宮
maze = [[1,1,1,1,1,1,1],
        [1,0,0,0,0,0,3],
        [1,0,1,0,1,0,1],
        [0,0,1,0,0,0,1],
        [1,0,1,0,1,0,1],
        [1,0,0,0,0,0,1],
        [1,2,1,0,1,0,1]]

# 要回傳 "Finish" 的測試資料
test.it("Should return Finish")
test.assert_equals(maze_runner(maze,["N","N","N","N","N","E","E","E","E","E"]), "Finish")
test.assert_equals(maze_runner(maze,["N","N","N","N","N","E","E","S","S","E","E","N","N","E"]), "Finish")
test.assert_equals(maze_runner(maze,["N","N","N","N","N","E","E","E","E","E","W","W"]), "Finish")

# 要回傳 "Dead" 的測試資料
test.it("Should return Dead")
test.assert_equals(maze_runner(maze,["N","N","N","W","W"]), "Dead")
test.assert_equals(maze_runner(maze,["N","N","N","N","N","E","E","S","S","S","S","S","S"]), "Dead")

# 要回傳 "Lost" 的測試資料
test.it("Should return Lost")
test.assert_equals(maze_runner(maze,["N","E","E","E","E"]), "Lost")