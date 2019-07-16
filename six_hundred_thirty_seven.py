# -*- coding: UTF-8 -*-

"""
# @Time    : 2019-07-13 09:44
# @Author  : yanlei
# @FileName: six_hundred_thirty_seven.py

给定一个非空二叉树, 返回一个由每层节点平均值组成的数组.

示例 1:

输入:
    3
   / \
  9  20
    /  \
   15   7
输出: [3, 14.5, 11]
解释:
第0层的平均值是 3,  第1层是 14.5, 第2层是 11. 因此返回 [3, 14.5, 11].

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/average-of-levels-in-binary-tree
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
nums = [3,9,20,15,7]

root = createTree(nums)


class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        levels = []
        if not root:
            return levels

        def helper(node, level):
            if level == len(levels):
                levels.append([])

            levels[level].append(node.val)
            if node.left:
                helper(node.left, level+1)
            if node.right:
                helper(node.right, level+1)
            return levels

        helper(root, 0)
        print(len(levels[1]))
        print(type(len(levels[1])))
        print(sum(levels[1]))
        print(type(sum(levels[1])))
        print(type(sum(levels[1])/len(levels[1])))
        # python2中 int 除 int 会默认得到int型 python3中只直接执行 / 就可以了  python2:return [sum(tmp)/len(tmp) for tmp in levels] --> [3.0, 14.0, 11.0]
        return [sum(tmp)/float(len(tmp)) for tmp in levels]

        # return [sum(tmp) / len(tmp) for tmp in levels]
        # [3.0, 14.5, 11.0]


print(Solution().averageOfLevels(root))
