# -*- coding: UTF-8 -*-

"""
# @Time    : 2019-07-12 09:31
# @Author  : yanlei
# @FileName: one_hundred_one.py
给定一个二叉树，检查它是否是镜像对称的。

例如，二叉树 [1,2,2,3,4,4,3] 是对称的。

    1
   / \
  2   2
 / \ / \
3  4 4  3
但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:

    1
   / \
  2   2
   \   \
   3    3

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/symmetric-tree
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
nums = [1,2,3]

root = createTree(nums)


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # 迭代
        # 时间复杂度 o(n)
        # 空间复杂度 o(n)
        queue = [root, root]
        while queue:
            q2 = queue.pop()
            q1 = queue.pop()
            if not q2 and not q1:
                continue
            if not q2 or not q1:
                return False
            if q1.val != q2.val:
                return False
            queue.append(q1.left)
            queue.append(q2.right)
            queue.append(q1.right)
            queue.append(q2.left)

        return True
        # 递归
        # 时间复杂度 o(n)
        # 空间复杂度 o(n)
        # def judgeSymmetric(root1, root2):
        #     if not root1 and not root2:
        #         return True
        #     if not root1 or not root2:
        #         return False
        #     return root1.val == root2.val and judgeSymmetric(root1.left, root2.right) and judgeSymmetric(root1.right, root2.left)
        # return judgeSymmetric(root.left, root.right)



print(Solution().isSymmetric(root))
