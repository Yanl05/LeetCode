# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        lenh = 0
        t = head
        while t.next != None:
            t = t.next
            lenh += 1   
        x = lenh - n
        xnode = head
        if x < 0:
            head = head.next
            return head
        while x:
            xnode = xnode.next
            x -= 1
        xnode.next = xnode.next.next
            
        return head
