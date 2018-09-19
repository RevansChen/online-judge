# Python3

def bishopAndPawn(bishop, pawn):
    getPos = lambda s: ('abcdefgh'.index(s[0]), '12345678'.index(s[1]))
    bishopPos = getPos(bishop)
    pawnPos = getPos(pawn)
    return abs(bishopPos[0] - pawnPos[0]) == abs(bishopPos[1] - pawnPos[1])
