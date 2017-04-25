from functools import reduce

class Connect4():
    MAX_COLUMN = 7
    MAX_ROW = 6
    CONNECT_NUM = 4
    
    EMPTY = 0
    PLAYER_1 = 1
    PLAYER_2 = 2
    
    def __init__(self):
        self.grid = [[Connect4.EMPTY] * Connect4.MAX_COLUMN for i in range(Connect4.MAX_ROW)]
        self.player = Connect4.PLAYER_1
        self.finished = False
        
        self.groups = []
        for col in range(Connect4.MAX_COLUMN):
            for row in range(Connect4.MAX_ROW - Connect4.CONNECT_NUM + 1):
                self.groups.append([ (r, col) for r in range(row, row + Connect4.CONNECT_NUM) ])
        for row in range(Connect4.MAX_ROW):
            for col in range(Connect4.MAX_COLUMN - Connect4.CONNECT_NUM + 1):
                self.groups.append([ (row, c) for c in range(col, col + Connect4.CONNECT_NUM) ])
        for row in range(Connect4.MAX_ROW - Connect4.CONNECT_NUM + 1):
            for col in range(Connect4.MAX_COLUMN - Connect4.CONNECT_NUM + 1):
                self.groups.append([ (row + i, col + i) for i in range(Connect4.CONNECT_NUM) ])
            for col in range(Connect4.MAX_COLUMN - 1, Connect4.MAX_COLUMN - 1 - Connect4.CONNECT_NUM, -1):
                self.groups.append([ (row + i, col - i) for i in range(Connect4.CONNECT_NUM) ])
    
    def __check(self):
        chk = lambda x,y: 0 if x != y else x
        
        for group in self.groups:
            line = [ self.grid[r][c] for r, c in group ]
            win = reduce(chk, line)
            if win != Connect4.EMPTY:
                return win
        return 0
        
    def play(self, col):
        if self.finished:
            return 'Game has finished!'
            
        if self.grid[0][col] != Connect4.EMPTY:
            return 'Column full!'
            
        for row in range(1, Connect4.MAX_ROW + 1):
            if self.grid[-row][col] == Connect4.EMPTY:
                self.grid[-row][col] = self.player
                break
        
        self.finished = (self.__check() > 0)
        if self.finished:
            return 'Player %d wins!' % self.player
        else:
            x = 'Player %d has a turn' % self.player
            self.player = Connect4.PLAYER_1 if self.player == Connect4.PLAYER_2 else Connect4.PLAYER_2
            return x