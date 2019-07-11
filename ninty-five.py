# -*- coding: UTF-8 -*-

"""
# @Time    : 2019-05-29 10:33
# @Author  : yanlei
# @FileName: ninty-five.py

method: DFS
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
    #     if n == 0:
    #         return []
    #     return self.help(1, n)
    # def help(self, start, end):
    #     if start > end:
    #         return [None]
    #
    #     res = []
    #     for curr_root in range(start, end + 1):
    #         left = self.help(start, curr_root - 1)
    #         right = self.help(curr_root + 1, end)
    #
    #         for l in left:
    #             for r in right:
    #                 root = TreeNode(curr_root)
    #                 root.left = l
    #                 root.right = r
    #                 res.append(root)
    #     return res

        # 递归
        def generate_trees(start, end):
            if start > end:
                return [None, ]
            all_trees = []

            for i in range(start, end+1):  # pick up a root
                left_trees = generate_trees(start, i-1)
                right_trees = generate_trees(i+1, end)

                # connect left and right subtrees to the root i
                for l in left_trees:
                    for r in right_trees:
                        current_tree = TreeNode(i)
                        current_tree.left = l
                        current_tree.right = r
                        all_trees.append(current_tree)
            return all_trees


        return generate_trees(1, n) if n else []


print(Solution().generateTrees(3))
