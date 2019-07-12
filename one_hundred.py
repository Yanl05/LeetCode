# -*- coding: UTF-8 -*-

"""
# @Time    : 2019-07-12 10:10
# @Author  : yanlei
# @FileName: one_hundred.py

给定两个二叉树，编写一个函数来检验它们是否相同。

如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。

示例 1:

输入:       1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]

输出: true
示例 2:

输入:      1          1
          /           \
         2             2

        [1,2],     [1,null,2]

输出: false

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/same-tree
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def createTree(nodelist):
    """
    传入一个list， 使用层序便利创建二叉树
    :param nodelist:
    :return:
    """
    if nodelist == []:
        return None
    head = TreeNode(nodelist[0])
    Nodes = [head]
    j = 1
    for node in Nodes:
        if node != None:
            node.left = TreeNode(nodelist[j]) if nodelist[j] != None else None
            Nodes.append(node.left)
            j += 1
            if j == len(nodelist):
                return head
            node.right = TreeNode(nodelist[j]) if nodelist[j] != None else None
            Nodes.append(node.right)
            j += 1
            if j == len(nodelist):
                return head


# 构建二叉树
# nums = [1,2,2,3,4,4,3]
nums1 = [1, 2]
nums2 = [1, 2]

p = createTree(nums1)
q = createTree(nums2)


class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """

        # 迭代 一
        # if not p and not q:
        #     return True
        # if not p or not q:
        #     return False
        # stack_p = []
        # stack_q = []
        # while p or stack_p:
        #     while p and q:
        #         if p.val != q.val:
        #             return False
        #         stack_p.append(p)
        #         p = p.left
        #         stack_q.append(q)
        #         q = q.left
        #     if q or p:
        #         return False
        #     p = stack_p.pop()
        #     q = stack_q.pop()
        #
        #     p = p.right
        #     q = q.right
        # return True

        # 迭代二
        # queue = [p, q]
        # while queue:
        #     q2 = queue.pop()
        #     q1 = queue.pop()
        #     if not q1 and not q2:
        #         continue
        #     if not q1 or not q2:
        #         return False
        #     if q1.val != q2.val:
        #         return False
        #     queue.append(q1.left)
        #     queue.append(q2.left)
        #     queue.append(q1.right)
        #     queue.append(q2.right)
        # return True

        # 递归
        def judgeSame(p, q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            judgeSame(p.left, q.left)
            judgeSame(p.right, q.right)
            return p.val == q.val and judgeSame(p.left, q.left) and judgeSame(p.right, q.right)

        return judgeSame(p, q)


print(Solution().isSameTree(p, q))
