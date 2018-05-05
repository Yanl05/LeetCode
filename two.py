# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        def setNext(self,newnext):
            self.next=newnext
        head, p1, p2 = ListNode(0), l1, l2
        tail = head
        jw = 0  #进位为假，说明没有进位，直接两数相加，再判断结果是否大于10；进位为真，两数相加再加1，再判断结果是否大于10
        while p1 and p2:
            num = p1.val + p2.val +jw
            if num > 9:
                num -= 10
                jw = 1
            else:
                jw = 0
            # 添加节点
            tail.next = ListNode(num)
            tail = tail.next
            
            p1 = p1.next
            p2 = p2.next
            
        if p2:
            p1 = p2
        while p1:
            num = p1.val + jw
            if num > 9:
                num -= 10
                jw = 1
            else:
                jw = 0

            tail.next = ListNode(num)
            tail = tail.next

            p1 = p1.next

        if jw:
            tail.next = ListNode(1)
            tail = tail.next

        tail.next = None
        return head.next
            
            
