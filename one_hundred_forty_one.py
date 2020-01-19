# -*- coding: UTF-8 -*-

"""
# @Time    : 2020-01-19 08:45
# @Author  : yanlei
# @FileName: one_hundred_forty_one.py


"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    # 哈希
    # def hasCycle(self, head):
    #     """
    #     :type head: ListNode
    #     :rtype: bool
    #     """
    #     if not head:
    #         return False
    #     visited = set()
    #     while head.next is not None:
    #         if head.next in visited:
    #             return True
    #         else:
    #             visited.add(head)
    #         head = head.next
    #     return False


    # 快慢指针
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None or head.next is None:
            return False

        slow = head
        fast = head.next
        while slow != fast:
            if fast == None or fast.next == None:
                return False
            slow = slow.next
            fast = fast.next.next
        return True
