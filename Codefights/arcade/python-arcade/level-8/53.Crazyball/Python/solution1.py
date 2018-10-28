# Python3

# 有限制修改區域
from itertools import combinations

def crazyball(players, k):
    return [*combinations(sorted(players), k)]
