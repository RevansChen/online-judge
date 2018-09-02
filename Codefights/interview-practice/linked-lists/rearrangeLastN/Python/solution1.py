# Python3

# Definition for singly-linked list:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def rearrangeLastN(l, n):
    if n == 0 or l == []:
        return l
    
    count, curr = 0, l
    while curr:
        count += 1
        if curr.next:
            curr = curr.next
        else:
            curr.next = l
            break
            
    count -= n
    while count:
        curr = curr.next
        count -= 1
    l, curr.next = curr.next, None
    return l
