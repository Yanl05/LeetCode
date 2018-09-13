class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        lenn = len(nums)
        if lenn == 0:
            return [-1, -1]
        low = 0
        high = lenn - 1
        ret = [-1, -1]
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] < target:
                low = mid + 1
                continue
            elif nums[mid] > target:
                high = mid - 1
                continue
            elif nums[mid] == target:
                ret = [mid, mid]      
                low = mid - 1
                while low >= 0 and nums[low] == target:
                    ret[0] = low
                    low -= 1
                high = mid + 1
                while high < lenn and nums[high] == target:
                    ret[1] = high
                    high +=1
                return ret
        return ret
