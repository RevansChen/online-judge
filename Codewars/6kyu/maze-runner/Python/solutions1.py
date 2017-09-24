# Python - 3.4.3

WALL = 1
START_POINT = 2
FINISH_POINT = 3
dirs = {
    'W': (0, -1),
    'E': (0, 1),
    'N': (-1, 0),
    'S': (1, 0)
}
    
# 尋找起點
def find_maze_start_point(maze):
    for row in range(len(maze)):
        for col in range(len(maze[0])):
            if maze[row][col] == START_POINT:
                return (row, col)
    return None

def maze_runner(maze, directions):
    r, c = find_maze_start_point(maze)
    for direction in directions:
        dr, dc = dirs[direction]
        r += dr
        c += dc
        if (0 <= r < len(maze)) and (0 <= c < len(maze[0])):
            if maze[r][c] == WALL:
                # 撞到牆壁回傳 "Dead"
                return 'Dead'
            elif maze[r][c] == FINISH_POINT:
                # 走到終點回傳 "Finish"
                return 'Finish'
        else:
            # 走到地圖外回傳 "Dead"
            return 'Dead'
    # 沒有走到終點回傳 "Lost"
    return 'Lost'
