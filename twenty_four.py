# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return head
        if head.next == None:
            return head
        sta = ListNode(0)
        
        res = head.next
        i = 1
        while i % 2 == 1:
            if head.next == None:
                break
            
            tem = head.next
            head.next = tem.next            
            tem.next = head
            
            sta.next = tem
            sta = head
            
            if i == 1:
                res = tem
            
            if head.next == None:
                break
            head = head.next
            
            i = i + 2
        return res
        
        
       
