class Solution:
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # if not nums or len(nums) < 2:
        #     return 0
        # res = 0
        # curMaxArea = 0
        # maxNext = 0
        # for i in range(len(nums) - 1):
        #     maxNext = max(maxNext, i + nums[i])
        #     if i == curMaxArea:
        #         res += 1
        #         curMaxArea = maxNext
        # return res

        # if not nums or len(nums) < 2:
        #     return 0
        # level = 0
        # curMaxAera = 0
        # maxNext = 0
        # i = 0
        # while curMaxAera - i + 1 > 0:
        #     level += 1
        #     for j in range(i, curMaxAera + 1):
        #     # while i <= curMaxAera:
        #         maxNext = max(maxNext, nums[j] + j)
        #         if maxNext >= len(nums) - 1:
        #             return level
        #
        #     i = curMaxAera + 1
        #     curMaxAera = maxNext
        # return 0

        if not nums or len(nums) < 2:
            return 0
        ret = 0
        curMaxArea = 0
        maxNext = 0
        for i in range(len(nums) - 1):
            maxNext = max(maxNext, i + nums[i])
            if i == curMaxArea:
                ret += 1
                curMaxArea = maxNext
        return ret

print(Solution().jump([2,3,1,1,4]))
