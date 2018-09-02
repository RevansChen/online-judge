# Python3

# Definition for singly-linked list:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def mergeTwoLinkedLists(l1, l2):
    if l1 and l2:
        ans, l1, l2 = (ListNode(l1.value), l1.next, l2) if l1.value <= l2.value else (ListNode(l2.value), l1, l2.next)
        l = ans
        while l1 or l2:
            if l1 and l2:
                l.next, l1, l2 = (ListNode(l1.value), l1.next, l2) if l1.value <= l2.value else (ListNode(l2.value), l1, l2.next)
                l = l.next
            else:
                l.next = l1 or l2
                break
        return ans
    return l1 or l2
