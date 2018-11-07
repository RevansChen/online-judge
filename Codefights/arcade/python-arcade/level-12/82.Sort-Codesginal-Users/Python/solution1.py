# Python3

# 有限制修改區域
def sortCodesignalUsers(users):
    res = [CodeSignalUser(*user) for user in users]
    res.sort(reverse=True)
    return list(map(str, res))

class CodeSignalUser:
    def __init__(self, username, _id, xp):
        self.username = username
        self._id = int(_id)
        self.xp = int(xp)

    def __str__(self):
        return self.username

    def __lt__(self, others):
        if self.xp == others.xp:
            return self._id > others._id
        else:
            return self.xp < others.xp
