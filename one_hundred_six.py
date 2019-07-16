# -*- coding: UTF-8 -*-

"""
# @Time    : 2019-07-16 10:57
# @Author  : yanlei
# @FileName: one_hundred_six.py

根据一棵树的中序遍历与后序遍历构造二叉树。

注意:
你可以假设树中没有重复的元素。

例如，给出

中序遍历 inorder = [9,3,15,20,7]
后序遍历 postorder = [9,15,7,20,3]
返回如下的二叉树：

    3
   / \
  9  20
    /  \
   15   7

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        def helper(in_left=0, in_right=len(inorder)):

            nonlocal post_idx

            if in_left == in_right:
                return None
            # pick up post_idx as a root
            root_val = postorder[post_idx]
            root = TreeNode(root_val)

            # root split inorder list
            index = idx_map[root_val]

            post_idx -= 1
            root.right = helper(index + 1, in_right)
            root.left = helper(in_left, index)
            return root

        post_idx = len(postorder) - 1
        idx_map = {val: idx for idx, val in enumerate(inorder)}
        return helper()


postorder = [9,15,7,20,3]
inorder = [9,3,15,20,7]
print(Solution().buildTree(inorder, postorder))
