def find_maze_start_point(maze):
    for row in range(len(maze)):
        for col in range(len(maze[0])):
            if maze[row][col] == 2:
                return (row, col)
    return None

def maze_runner(maze, directions):
    dirs = {
        'W': (0, -1),
        'E': (0, 1),
        'N': (-1, 0),
        'S': (1, 0)
    }
    
    row, col = find_maze_start_point(maze)
    r, c = 0, 0
    for direction in directions:
        dr, dc = dirs[direction]
        r, c = row + dr, col + dc
        if (0 <= r < len(maze)) and (0 <= c < len(maze[0])):
            if maze[r][c] == 1:
                return 'Dead'
            elif maze[r][c] == 3:
                return 'Finish'
            row, col = r, c
        else:
            return 'Dead'
    return 'Finish' if maze[r][c] == 3 else 'Lost'