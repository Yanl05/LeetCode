# -*- coding: UTF-8 -*-

"""
# @Time    : 2019/8/14 
# @Author  : yanlei
# @FileName: one_hundred_thirteen.py

给定一个二叉树和一个目标和，找到所有从根节点到叶子节点路径总和等于给定目标和的路径。

说明: 叶子节点是指没有子节点的节点。

示例:
给定如下二叉树，以及目标和 sum = 22，

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
返回:

[
   [5,4,11,2],
   [5,8,4,5]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/path-sum-ii
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
nums = [5,4,8,11,None,13,4,7,2,None,None,5,1]
root = createTree(nums)


# 递归
class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        def recursion(p, count, tmp):
            nonlocal FLAG
            if p.left == None and p.right == None:
                count += p.val
                # print(count)
                if count == sum:
                    FLAG = True
                    tmp += [p.val]
                    ret.append(tmp)
                    return
            elif p.left == None:
                recursion(p.right, count+p.val, tmp+[p.val])
            elif p.right == None:
                recursion(p.left, count+p.val, tmp+[p.val])
            else:
                recursion(p.right, count+p.val, tmp+[p.val])
                recursion(p.left, count+p.val, tmp+[p.val])
        if not root:
            return False
        count = 0
        FLAG = False
        ret = []
        recursion(root, count, [])
        # if FLAG:
        #     return True
        return ret


print(Solution().pathSum(root, 22))