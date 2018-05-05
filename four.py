class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums3=nums1+nums2
        nums3 = sorted(nums3)
        lennums = len(nums3)
        if lennums % 2 == 0:
            return (nums3[lennums//2 -1]+nums3[lennums//2])/2
        else:
            return nums3[lennums//2]
           
