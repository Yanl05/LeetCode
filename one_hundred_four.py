# -*- coding: UTF-8 -*-

"""
# @Time    : 2019-07-16 09:47
# @Author  : yanlei
# @FileName: one_hundred_four.py

给定一个二叉树，找出其最大深度。

二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。

说明: 叶子节点是指没有子节点的节点。

示例：
给定二叉树 [3,9,20,null,null,15,7]，

    3
   / \
  9  20
    /  \
   15   7
返回它的最大深度 3 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-depth-of-binary-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
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
nums = [3,9,20,None,None,15,7]
# nums = [1,2,3,4,None,None,5]
root = createTree(nums)

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        # 递归 DFS

        # 迭代 BFS
        if not root:
            return 0
        ret = []
        stack = [root]
        level = 0
        while stack:
            ret.append([])
            level_length = len(stack)
            for _ in range(level_length):
                p = stack.pop(0)
                ret[level].append(p.val)
                if p.left:
                    stack.append(p.left)
                if p.right:
                    stack.append(p.right)
            level += 1

        return level


print(Solution().maxDepth(root))

