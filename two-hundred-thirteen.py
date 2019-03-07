class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        ret1 = self.robson(nums[:-1])
        ret2 = self.robson(nums[1:])
        return max(ret1, ret2)

    def robson(self, nums):
        if not nums:
            return 0
        D = [0 for _ in nums]
        for index, num in enumerate(nums):
            if index == 0:
                D[index] = num
            elif index == 1:
                D[index] = max(D[index-1], num)
            else:
                D[index] = max((D[index-2]+num), D[index-1])
        return D[-1]




print(Solution().rob([1]))