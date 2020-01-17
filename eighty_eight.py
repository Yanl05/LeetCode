# -*- coding: UTF-8 -*-

"""
# @Time    : 2019-10-27 17:07
# @Author  : yanlei
# @FileName: eighty_eight.py

给定两个有序整数数组 nums1 和 nums2，将 nums2 合并到 nums1 中，使得 num1 成为一个有序数组。

说明:

初始化 nums1 和 nums2 的元素数量分别为 m 和 n。
你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。
示例:

输入:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

输出: [1,2,2,3,5,6]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/merge-sorted-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
# 快排
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        for i in range(n):
            nums1[m+i] = nums2[i]
        nums1 = nums1[:m+n]
        print(nums1)
        return self.quick_sort(nums1)

    def quick_sort(self, array):
        # 递归入口及出口
        if len(array) >= 2:
            mid = array[len(array)//2]  # 选取基准值，也可以选取第一个或者最后一个数
            left, right = [], []
            array.remove(mid)
            for num in array:
                if num >= mid:
                    right.append(num)
                else:
                    left.append(num)
            return self.quick_sort(left) + [mid] + self.quick_sort(right)
        else:
            return array


# 双指针，从后往前
# class Solution(object):
#     def merge(self, nums1, m, nums2, n):
#         """
#         :type nums1: List[int]
#         :type m: int
#         :type nums2: List[int]
#         :type n: int
#         :rtype: None Do not return anything, modify nums1 in-place instead.
#         """
#         # two get pointers for num1 and num2
#         p1 = m - 1
#         p2 = n - 1
#         # set pointer for num1
#         p = m + n - 1
#
#         while p1 >= 0 and p2 >= 0:
#             if nums1[p1] < nums2[p2]:
#                 nums1[p] = nums2[p2]
#                 p2 -= 1
#             else:
#                 nums1[p] = nums1[p1]
#                 p1 -= 1
#             p -= 1
#
#         # add missing elements from nums2
#         nums1[:p2+1] = nums2[:p2+1]
#         print(nums1)



print(Solution().merge([1,2,3,0,0,0], 3, [2,5,6],3))

