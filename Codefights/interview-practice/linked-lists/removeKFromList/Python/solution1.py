# coding: utf-8
# Python3

# Definition for singly-linked list:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def removeKFromList(l, k):
    head = ListNode(0)
    head.next = l
    now, prev = l, head
    while now:
        if now.value == k:
            prev.next = now.next
        else:
            prev = now
        now = now.next
    return head.next
