# -*- coding: UTF-8 -*-

"""
# @Time    : 2019-07-16 10:30
# @Author  : yanlei
# @FileName: one_hundred_five.py

根据一棵树的前序遍历与中序遍历构造二叉树。

注意:
你可以假设树中没有重复的元素。

例如，给出

前序遍历 preorder = [3,9,20,15,7]
中序遍历 inorder = [9,3,15,20,7]
返回如下的二叉树：

    3
   / \
  9  20
    /  \
   15   7

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        def helper(in_left=0, in_right=len(inorder)):
            nonlocal pre_idx
            if in_left == in_right:
                return None

            # pick up pre_idx as a root
            root_val = preorder[pre_idx]
            root = TreeNode(root_val)

            # root split inorder list
            index = idx_map[root_val]

            pre_idx +=1
            root.left = helper(in_left, index)
            root.right = helper(index+1,in_right)
            return root


        # preorder 的第一个元素
        pre_idx = 0
        idx_map = {val:idx for idx, val in enumerate(inorder)}
        return helper()


preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
print(Solution().buildTree(preorder, inorder))