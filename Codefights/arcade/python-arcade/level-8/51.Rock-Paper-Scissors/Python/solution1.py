# Python3

# 有限制修改區域
from itertools import permutations

def rockPaperScissors(players):
    return sorted(permutations(players, 2))
