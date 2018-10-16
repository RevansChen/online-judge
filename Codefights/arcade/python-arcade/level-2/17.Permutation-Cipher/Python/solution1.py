# Python3

# 有限制修改區域
def permutationCipher(password, key):
    table = str.maketrans(''.join(map(chr, range(ord('a'), ord('z') + 1))), key)
    return password.translate(table)
