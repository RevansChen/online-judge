# coding: utf-8
# Python3

# Definition for singly-linked list:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def reverseNodesInKGroups(l, k):
    curr, selected = l, []
    while curr:
        selected.append(curr)
        if len(selected) >= k:
            for left in range(k >> 1):
                right = -(left + 1)
                selected[left].value, selected[right].value = selected[right].value, selected[left].value
            selected = []
        curr = curr.next
    return l
