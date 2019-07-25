# -*- coding: UTF-8 -*-

"""
# @Time    : 2019-07-25 09:34
# @Author  : yanlei
# @FileName: one_hundred_eleven.py

给定一个二叉树，找出其最小深度。

最小深度是从根节点到最近叶子节点的最短路径上的节点数量。

说明: 叶子节点是指没有子节点的节点。

示例:

给定二叉树 [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回它的最小深度  2.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-depth-of-binary-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def createTree(nums):
    if not nums:
        return None
    root = TreeNode(nums[0])
    stack = [root]
    j = 1
    while stack:
        lens = len(stack)
        for i in range(lens):
            p = stack.pop(0)
            if nums[j] != None:
                p.left = TreeNode(nums[j])
                stack.append(p.left)
            j += 1
            if j == len(nums):
                return root
            if nums[j] != None:
                p.right = TreeNode(nums[j])
                stack.append(p.right)
            j += 1
            if j == len(nums):
                return root
# root = createTree([3,None,20])
root = createTree([3,9,20,None,None,15,7])
# print(root.left.val)


class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        min_depth = float('inf')
        min_depth = self.helper(root, min_depth)
        return min_depth

    def helper(self, p,  min_depth):
        if not p:
            return 0
        if p.left == None and p.right == None:
            return 1
        if p.left != None:
            min_depth = min(self.helper(p.left, min_depth)+1, min_depth)
        if p.right != None:
            min_depth = min(self.helper(p.right, min_depth)+1, min_depth)
        return min_depth

        # if not root:
        #     return 0
        #
        # children = [root.left, root.right]
        # if not any(children):
        #     return 1
        #
        # min_depth = float('inf')
        # for c in children:
        #     if c:
        #         min_depth = min(self.minDepth(c), min_depth)
        # return min_depth+1


print(Solution().minDepth(root))
