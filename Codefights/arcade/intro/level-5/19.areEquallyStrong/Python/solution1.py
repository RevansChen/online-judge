# Python3

def areEquallyStrong(yourLeft, yourRight, friendsLeft, friendsRight):
    if yourLeft > yourRight:
        yourLeft, yourRight = yourRight, yourLeft
    if friendsLeft > friendsRight:
        friendsLeft, friendsRight = friendsRight, friendsLeft
    return (yourLeft == friendsLeft) and (yourRight == friendsRight)
