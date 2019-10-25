# -*- coding: UTF-8 -*-

"""
# @Time    : 2019-10-25 12:08
# @Author  : yanlei
# @FileName: two_hundred_six.py

反转一个单链表。

示例:

输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL
进阶:
你可以迭代或递归地反转链表。你能否用两种方法解决这道题？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-linked-list
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
print(root.val)

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # pre = ListNode(None)
        # 1. 迭代
        pre = None
        cur = head
        next = head
        while cur != None:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next
        return pre

        # 2.递归



new_root = Solution().reverseList(root)
print(new_root.val)
