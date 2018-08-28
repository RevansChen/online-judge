# coding: utf-8
# Python3

# Definition for singly-linked list:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def isListPalindrome(l):
    ls = []
    while l:
        ls.append(l.value)
        l = l.next
    return ls == ls[::-1] if ls else True
