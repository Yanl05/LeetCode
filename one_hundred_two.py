# -*- coding: UTF-8 -*-

"""
# @Time    : 2019-07-13 08:51
# @Author  : yanlei
# @FileName: one_hundred_two.py

给定一个二叉树，返回其按层次遍历的节点值。 （即逐层地，从左到右访问所有节点）。

例如:
给定二叉树: [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其层次遍历结果：

[
  [3],
  [9,20],
  [15,7]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-level-order-traversal
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
# nums = [3,9,20,None,None,15,7]
nums = [1,2,3,4,5]

root = createTree(nums)


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # 迭代
        # 时间复杂度、空间复杂度 o(n)
        # ret = []
        # if not root:
        #     return ret
        # stack = [root]
        # level = 0
        # while stack:
        #     ret.append([])
        #     level_length = len(stack)
        #     for _ in range(level_length):
        #         p = stack.pop(0)
        #         ret[level].append(p.val)
        #
        #         if p.left:
        #             stack.append(p.left)
        #         if p.right:
        #             stack.append(p.right)
        #     level += 1
        # return ret

        # 递归
        # 时间复杂度、空间复杂度 o(n)
        levels = []
        if not root:
            return levels

        def helper(node, level):
            if len(levels) == level:
                levels.append([])
            levels[level].append(node.val)

            if node.left:
                helper(node.left, level+1)
            if node.right:
                helper(node.right, level+1)


        helper(root, 0)
        return levels



print(Solution().levelOrder(root))