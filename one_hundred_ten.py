# -*- coding: UTF-8 -*-

"""
# @Time    : 2019-07-17 10:12
# @Author  : yanlei
# @FileName: one_hundred_ten.py

给定一个二叉树，判断它是否是高度平衡的二叉树。

本题中，一棵高度平衡二叉树定义为：

一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过1。

示例 1:

给定二叉树 [3,9,20,null,null,15,7]

    3
   / \
  9  20
    /  \
   15   7
返回 true 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/balanced-binary-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
# 给定一个数组，创建对应的树
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class createTree:
    def __init__(self, nums):
        self.nums = nums
    def create(self):
        # 使用层序遍历创建树
        if not self.nums:
            return None
        head =TreeNode(self.nums[0])
        if len(self.nums) == 1:
            return head
        Nodes = [head]
        j = 1
        while Nodes:
            tmproot = Nodes.pop(0)
            tmproot.left = TreeNode(self.nums[j]) if self.nums[j] != None else None
            Nodes.append(tmproot.left)
            j += 1
            if j == len(self.nums):
                return head
            tmproot.right = TreeNode(self.nums[j]) if self.nums[j] != None else None
            Nodes.append(tmproot.right)
            j+=1
            if j == len(self.nums):
                return head
# nums = [3,9,20,None,None,15,7]
nums = [3]
root = createTree(nums).create()
print(root)

# 层序遍历输出树的节点
# 迭代
def sequenceTree(root):
    ret = []
    if not root:
        return ret
    stack = [root]
    subSequence = []
    while stack:
        for _ in range(len(stack)):
            tmproot = stack.pop(0)
            subSequence.append(tmproot.val)
            if tmproot.left:
                stack.append(tmproot.left)
            if tmproot.right:
                stack.append(tmproot.right)
        ret.append(subSequence)
        subSequence = []
    return ret
print(sequenceTree(root))





class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # 自顶向下
        # if not root:
        #     return True
        # return abs(self.maxDeoth(root.left)-self.maxDeoth(root.right))<2 and self.isBalanced(root.left) and self.isBalanced(root.right)

        # 自底向上
        self.res = True
        def helper(root):
            if not root:
                return 0
            left = helper(root.left)+1
            right = helper(root.right) + 1

            if abs(right - left) > 1:
                self.res = False
            return max(left, right)
        helper(root)
        return self.res

    def maxDeoth(self, root):
        # 迭代
        # level = 0
        # if not root:
        #     return level
        # stack = [root]
        # while stack:
        #     level_length = len(stack)
        #     for _ in range(level_length):
        #         p = stack.pop(0)
        #         if p.left:
        #             stack.append(p.left)
        #         if p.right:
        #             stack.append(p.right)
        #     level += 1
        # return level

        # 递归
        if not root:
            return 0
        return 1 + max(self.maxDeoth(root.left), self.maxDeoth(root.right))

print(Solution().maxDeoth(root))
print(Solution().isBalanced(root))

