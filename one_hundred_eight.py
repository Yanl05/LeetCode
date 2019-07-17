# -*- coding: UTF-8 -*-

"""
# @Time    : 2019-07-17 08:55
# @Author  : yanlei
# @FileName: one_hundred_eight.py

将一个按照升序排列的有序数组，转换为一棵高度平衡二叉搜索树。

本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。

示例:

给定有序数组: [-10,-3,0,5,9],

一个可能的答案是：[0,-3,9,-10,null,5]，它可以表示下面这个高度平衡二叉搜索树：

      0
     / \
   -3   9
   /   /
 -10  5

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/convert-sorted-array-to-binary-search-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        # 递归
        # def helper(l=0, r=len(nums)):
        #     if l >= r:
        #         return None
        #     # 创建根节点
        #     mid = (l+r)//2
        #     print(mid)
        #     root_val = nums[mid]
        #     root = TreeNode(root_val)
        #
        #     root.left = helper(l, mid)
        #     root.right = helper(mid+1, r)
        #
        #     return root
        #
        # if len(nums) == 0:
        #     return None
        # return helper()

        # 中序遍历创建二叉搜索树
        def inorder(root):
            nonlocal i
            if not root:
                return
            inorder(root.left)
            root.val = nums[i]
            i += 1
            inorder(root.right)

        if not nums:
            return None
        lenTree = len(nums)
        root = TreeNode(-1)
        q = [root]
        while q:
            for _ in range(len(q)):
                tmproot = q.pop(0)
                lenTree -= 1
                if lenTree>0:
                    tmproot.left = TreeNode(-1)
                    q.append(tmproot.left)
                lenTree -= 1
                if lenTree>0:
                    tmproot.right = TreeNode(-1)
                    q.append(tmproot.right)
        i = 0
        inorder(root)

        # 层次遍历，查看树的值
        # 递归
        # ret = []
        # level = 0
        # def getVal(node, level):
        #     if len(ret) == level:
        #         ret.append([])
        #     ret[level].append(node.val)
        #     if node.left:
        #         getVal(node.left, level+1)
        #     if node.right:
        #         getVal(node.right, level+1)
        # getVal(root, level)
        # print(ret)
        return root






print(Solution().sortedArrayToBST([-10,-3,0,5,9]))