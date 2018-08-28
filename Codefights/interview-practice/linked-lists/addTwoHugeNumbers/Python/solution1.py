# coding: utf-8
# Python3

# Definition for singly-linked list:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def addTwoHugeNumbers(a, b):
    def linkedListToList(linkedList):
        ls, node = [], linkedList
        while node:
            ls.append(node.value)
            node = node.next
        return ls
    
    la, lb = linkedListToList(a), linkedListToList(b)
    ans, lst = (la.copy(), lb) if len(la) > len(lb) else (lb.copy(), la)
    
    for i in range(1, len(lst) + 1):
        ans[-i] += lst[-i]
        
    ans = [0] + ans
    for i in range(1, len(ans)):
        ans[-(i + 1)] += ans[-i] // 10000
        ans[-i] = ans[-i] % 10000
        
    return ans if ans[0] else ans[1:]
