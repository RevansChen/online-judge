# Python - 3.4.3

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
        
        # 列出所有要檢查的位置
        self.groups = []
        # 垂直線
        for col in range(Connect4.MAX_COLUMN):
            for row in range(Connect4.MAX_ROW - Connect4.CONNECT_NUM + 1):
                self.groups.append([ (r, col) for r in range(row, row + Connect4.CONNECT_NUM) ])
        # 水平線
        for row in range(Connect4.MAX_ROW):
            for col in range(Connect4.MAX_COLUMN - Connect4.CONNECT_NUM + 1):
                self.groups.append([ (row, c) for c in range(col, col + Connect4.CONNECT_NUM) ])
        # 斜線
        for row in range(Connect4.MAX_ROW - Connect4.CONNECT_NUM + 1):
            for col in range(Connect4.MAX_COLUMN - Connect4.CONNECT_NUM + 1):
                self.groups.append([ (row + i, col + i) for i in range(Connect4.CONNECT_NUM) ])
            for col in range(Connect4.MAX_COLUMN - 1, Connect4.MAX_COLUMN - 1 - Connect4.CONNECT_NUM, -1):
                self.groups.append([ (row + i, col - i) for i in range(Connect4.CONNECT_NUM) ])
    
    def __check(self):
        chk = lambda x,y: Connect4.EMPTY if x != y else x
        
        # 列舉所有要檢查的位置，若有發現玩家勝利則回傳該玩家的編號
        for group in self.groups:
            line = [ self.grid[r][c] for r, c in group ]
            win = reduce(chk, line)
            if win != Connect4.EMPTY:
                return win
        return Connect4.EMPTY
        
    def play(self, col):
        # 遊戲結束後，若再放入棋子則顯示"Game has finished!"
        if self.finished:
            return 'Game has finished!'
        
        # 任一列全滿時，若再放入棋子則顯示"Column full!"
        if self.grid[0][col] != Connect4.EMPTY:
            return 'Column full!'
            
        for row in range(1, Connect4.MAX_ROW + 1):
            if self.grid[-row][col] == Connect4.EMPTY:
                self.grid[-row][col] = self.player
                break
        
        self.finished = (self.__check() != Connect4.EMPTY)
        if self.finished:
            # 任一玩家讓四個棋子連成一線(垂直、水平或斜線)即獲勝，並顯示"Player n wins!" (n為1或2，表示玩家一或玩家二)
            return 'Player %d wins!' % self.player
        else:
            # 任一玩家動作後，顯示"Player n has a turn" (n為1或2，表示玩家一或玩家二)
            x = 'Player %d has a turn' % self.player
            self.player = Connect4.PLAYER_1 if self.player == Connect4.PLAYER_2 else Connect4.PLAYER_2
            return x
