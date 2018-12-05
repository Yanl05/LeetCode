# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head == None or k == 0:
            return head
        dummy = ListNode(0)
        dummy.next = head
        # 计算链表长度
        count = 0
        p = dummy
        while p.next != None:
            p = p.next
            count += 1
        # 形成环形
        p.next = dummy.next
        # 求真实的右移数量
        right = count - k % count
        p = dummy.next
        for i in range(1, right):
            p = p.next
        head = p.next
        p.next = None
        return head
