# -*- coding: UTF-8 -*-

"""
# @Time    : 2019-07-12 10:34
# @Author  : yanlei
# @FileName: two_hundred_fifty_seven.py
给定一个二叉树，返回所有从根节点到叶子节点的路径。

说明: 叶子节点是指没有子节点的节点。

示例:

输入:

   1
 /   \
2     3
 \
  5

输出: ["1->2->5", "1->3"]

解释: 所有根节点到叶子节点的路径为: 1->2->5, 1->3

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-paths
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
nums = [1, 2, 3, None, 5]

root = createTree(nums)


class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        # 递归
        # 时间复杂度 o(n)
        # 空间复杂度 o(n) 最好情况下二叉树为平衡二叉树 树高为 log(N) 空间复杂度为o(log(N))
    #     res = []
    #     self.subTree(root, '', res)
    #     return res
    #
    # def subTree(self, root, subStr, res):
    #     if not root.left and not root.right:
    #         subStr += str(root.val)
    #         res.append(subStr)
    #         return None
    #     if not root.right:
    #         self.subTree(root.left, subStr + str(root.val)+'->', res)
    #     elif not root.left:
    #         self.subTree(root.right, subStr + str(root.val)+'->', res)
    #     else:
    #         self.subTree(root.left, subStr + str(root.val)+'->', res)
    #         self.subTree(root.right, subStr + str(root.val)+'->', res)

        # 迭代
        # 时间复杂度、空间复杂度 都为 o(n)
        if not root:
            return []

        paths = []
        stack = [(root, str(root.val))]
        while stack:
            node, path = stack.pop()
            if not node.left and not node.right:
                paths.append(path)
            if node.left:
                stack.append((node.left, path+'->'+str(node.left.val)))
            if node.right:
                stack.append((node.right, path + '->' + str(node.right.val)))
        return paths

print(Solution().binaryTreePaths(root))
