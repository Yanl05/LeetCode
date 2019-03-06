class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # if not nums:
        #     return 0
        # if len(nums) == 1:
        #     return nums[0]
        # if len(nums) == 2:
        #     return max(nums[0], nums[1])
        # dp = [0] * len(nums)
        # dp[0] = nums[0]
        # dp[1] = max(nums[0], nums[1])
        # for i in range(2, len(nums)):
        #     dp[i] = max((dp[i - 2] + nums[i]), dp[i - 1])
        # return dp

        if len(nums) == 0:
            return 0
        D = [0 for _ in nums]
        for index, num in enumerate(nums):
            if index == 0:
                D[index] = num
            elif index == 1:
                D[index] = max(D[index - 1], num)
            else:
                D[index] = max(D[index - 2] + num, D[index - 1])
        return D[-1]

print(Solution().rob([2,1,1,2]))
