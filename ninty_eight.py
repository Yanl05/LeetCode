# -*- coding: UTF-8 -*-

"""
# @Time    : 2019-07-09 11:57
# @Author  : yanlei
# @FileName: ninty_eight.py

给定一个二叉树，判断其是否是一个有效的二叉搜索树。

假设一个二叉搜索树具有如下特征：

节点的左子树只包含小于当前节点的数。
节点的右子树只包含大于当前节点的数。
所有左子树和右子树自身必须也是二叉搜索树。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/validate-binary-search-tree
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
nums = [2,1,3]
# nums = [5,1,4,None,None,3,6]
# nums = [5,1,6,None,None,4,7]
# nums = [5,1,6,None,None,4,7]
root = createTree(nums)

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # 递归
        # def helper(node, lower = float('-inf'), upper = float('inf')):
        #     if not node:
        #         return True
        #
        #     val = node.val
        #     if val <= lower or val >= upper:
        #         return False
        #     if not helper(node.right, val, upper):
        #         return False
        #     if not helper(node.left, lower, val):
        #         return False
        #     return True
        # return helper(root)


        return self.judgeBST(root)
    def judgeBST(self, subTree, lower = float('-inf'), upper = float('inf')):
        if not subTree:
            return True
        if subTree.val >= upper or subTree.val <= lower:
            return False
        if not self.judgeBST(subTree.left,lower,subTree.val):
            return False
        if not self.judgeBST(subTree.right, subTree.val, upper):
            return False
        return True

















print(Solution().isValidBST(root))

