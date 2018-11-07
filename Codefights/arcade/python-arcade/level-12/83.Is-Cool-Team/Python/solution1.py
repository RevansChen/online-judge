# Python3

# 有限制修改區域
class Team(object):
    def __init__(self, names):
        self.names = names

    def __bool__(self):
        count = {}
        for name in self.names:
            n = name.lower()
            count[n[0]] = count.get(n[0], 0) + 1
            count[n[-1]] = count.get(n[-1], 0) - 1
        count = { k: v for k, v in count.items() if v != 0 }
        return (len(count) == 2) or (not bool(count))

def isCoolTeam(team):
    return bool(Team(team))
