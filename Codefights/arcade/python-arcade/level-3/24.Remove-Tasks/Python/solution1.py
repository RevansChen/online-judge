# Python3

# 有限制修改區域
def removeTasks(k, toDo):
    del toDo[k - 1::k]
    return toDo
