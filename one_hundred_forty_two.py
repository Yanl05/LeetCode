# -*- coding: UTF-8 -*-

"""
# @Time    : 2020-01-20 08:46
# @Author  : yanlei
# @FileName: one_hundred_forty_two.py

环形链表2
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    # hash
    # def detectCycle(self, head):
    #     """
    #     :type head: ListNode
    #     :rtype: ListNode
    #     """
    #     if not head:
    #         return None
    #     visited = set()
    #     visited.add(head)
    #     while head.next is not None:
    #         if head.next not in visited:
    #             visited.add(head.next)
    #             head = head.next
    #         else:
    #             return head.next
    #     return None


    # 快慢指针
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 快慢指针
        # 阶段一： 判断是否有环
        if not head or not head.next:
            return None
        slow = head
        fast = head
        while True:
            if fast == None or fast.next == None:
                return None
            else:
                slow = slow.next
                fast = fast.next.next
            if slow == fast:
                meet = slow
                break
        # 阶段二： 判断入环口
        start_1 = head
        start_2 = meet
        while start_1 != start_2:
            start_1 = start_1.next
            start_2 = start_2.next
        return start_1