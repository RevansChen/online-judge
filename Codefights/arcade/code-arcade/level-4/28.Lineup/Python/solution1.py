# Python3

def lineUp(commands):
    count = 0
    table = { 'L': -1, 'R': 1, 'A': 2 }
    dir1, dir2 = 0, 0
    for cmd1, cmd2 in zip(commands, commands.translate({82: 76, 76: 82})):
        dir1 = (dir1 + table[cmd1]) % 4
        dir2 = (dir2 + table[cmd2]) % 4
        if dir1 == dir2:
            count += 1
    return count
