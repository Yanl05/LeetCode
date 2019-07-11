# -*- coding: UTF-8 -*-

"""
# @Time    : 2019-07-09 12:57
# @Author  : yanlei
# @FileName: ninety_four.py

给定一个二叉树，返回它的中序 遍历。

示例:

输入: [1,null,2,3]
   1
    \
     2
    /
   3

输出: [1,3,2]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-inorder-traversal
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
            node.right = TreeNode(nodelist[j] if nodelist[j] != None else None)
            Nodes.append(node.right)
            j += 1
            if j == len(nodelist):
                return head


class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # 递归
    #     res = []
    #     self.inorder(root, res)
    #     return res
    #
    # def inorder(self, root, res):
    #     if root:
    #         self.inorder(root.left, res)
    #         print(root.val)
    #         res.append(root.val)
    #         self.inorder(root.right, res)
    #         return None

        # 使用栈
        result = []
        stack = []
        while root or stack:
            if root:
                # 添加根节点对象到 栈 中
                stack.append(root)
                root = root.left  # 左
            else:
                root = stack.pop()  # 中
                result.append(root.val)
                root = root.right  # 右
        return result




# 构建二叉树
nums = [1, None, 2, 3]
root = createTree(nums)

print(Solution().inorderTraversal(root))
