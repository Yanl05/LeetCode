class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        lenn = len(nums)
        if lenn == 0:
            return 0
        if lenn == 1:
            if target <= nums[0]:
                return 0
            else:
                return 1
        low = 0; high = lenn - 1
        while low < high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                low = mid + 1
            # elif nums[mid] > target:
            else:
                high = mid - 1
        if target <= nums[low]:
            return low
        else:
            return low + 1
