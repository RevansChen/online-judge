# Python - 3.6.0

class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def append(listA, listB):
    if listA is None and listB is None:
        return None
    if listA is None:
        return listB
    if listB is None:
        return listA
    node = listA
    while node.next is not None:
        node = node.next
    node.next = listB
    return listA
