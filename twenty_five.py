# -*- coding: UTF-8 -*-

"""
# @Time    : 2019-10-25 14:32
# @Author  : yanlei
# @FileName: twenty_five.py

给你一个链表，每 k 个节点一组进行翻转，请你返回翻转后的链表。

k 是一个正整数，它的值小于或等于链表的长度。

如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。

示例 :

给定这个链表：1->2->3->4->5

当 k = 2 时，应当返回: 2->1->4->3->5

当 k = 3 时，应当返回: 3->2->1->4->5

说明 :

你的算法只能使用常数的额外空间。
你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-nodes-in-k-group
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
list = [1, 2, 3, 4, 5]
root = ListNode(list[0])
p = root
for num in list[1:]:
    p.next = ListNode(num)
    p = p.next
p.next = None

# 迭代
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head == None:
            return None
        a = head
        b = head
        for i in range(k):  # 将 a = head b = new_head
            if b == None:  # 不足k个， 不需要反转
                return head
            b = b.next
        newHead = self.reverse(a, b)
        a.next = self.reverseKGroup(b, k)
        return newHead
    def reverse(self, head, end):  # 左闭右开
        pre = None
        cur = head
        nxt = head
        while cur != end:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        return pre



new_root = Solution().reverseKGroup(root, 2)
print(new_root.val)