# Definition for singly-linked list.
'''
将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。
示例：
输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4
'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(4)

l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        输入：1->2->4, 1->3->4
        输出：1->1->2->3->4->4
        """
        head = ListNode(0)
        p = l1
        q = l2
        tail = head
        while p and q:
            if p.val < q.val:
                tail.next = ListNode(p.val)
                tail = tail.next
                p = p.next
            else:
                tail.next = ListNode(q.val)
                tail = tail.next
                q = q.next

        if q:
            p = q
        while p:
            tail.next = ListNode(p.val)
            tail = tail.next
            p = p.next

        tail.next = None

        t = head.next
        while 1:
            print(t.val)
            if t.next != None:
                t = t.next
            else:
                break

        return head.next


Solution().mergeTwoLists(l1, l2)


#p = Solution().mergeTwoLists()
# while 1:
#     print(p.val)
#     if p.next != None:
#         p = p.next
#     else:
#         break
