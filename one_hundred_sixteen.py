# -*- coding: UTF-8 -*-

"""
# @Time    : 2019-08-28 15:59
# @Author  : yanlei
# @FileName: one_hundred_sixteen.py

给定一个完美二叉树，其所有叶子节点都在同一层，每个父节点都有两个子节点。二叉树定义如下：

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 NULL。

初始状态下，所有 next 指针都被设置为 NULL。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/populating-next-right-pointers-in-each-node
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution(object):
    # 使用队列
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        from collections import deque
        if not root: return root
        queue = deque()
        queue.appendleft(root)
        while queue:
            p = None
            n = len(queue)
            for _ in range(n):
                tmp = queue.pop()
                if p:
                    p.next = tmp
                    p = p.next
                else:
                    p = tmp
                if tmp.left:
                    queue.appendleft(tmp.left)
                if tmp.right:
                    queue.appendleft(tmp.right)
            p.next = None
        return root

    # 递归
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return root
        if root.left:
            root.left.next = root.right
            if root.next:
                root.right.next = root.next.left
        self.connect(root.left)
        self.connect(root.right)
        return root

    # 迭代
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        pre = root
        while pre:
            cur = pre
            while cur:
                if cur.left:
                    cur.left.next = cur.right
                if cur.right and cur.next:
                    cur.right.next = cur.next.left
                cur = cur.next
            pre = pre.left
        return root



