class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        """o(nlogn)"""
        # judge = [0]*len(nums)
        # judge[0] = 1
        # for i in range(len(nums)-1):
        #     tmp = nums[i]
        #     tmpi = i + 1
        #     while tmp:
        #         if judge[i] > 0:
        #             judge[tmpi] += 1
        #             tmpi += 1
        #             if tmpi > len(nums)-1:
        #                 break
        #         tmp -= 1
        # print(judge)
        # if judge[-1] == 0:
        #     return False
        # else:
        #     return True

        """o(nlogn)"""
        # judge = [False] * len(nums)
        # judge[0] = True
        # for i in range(len(nums) - 1):
        #     tmp = nums[i]
        #     tmpi = i + 1
        #     for j in range(tmp, 0, -1):
        #         if tmpi <= len(nums) - 1 and judge[tmpi - 1] == True:
        #             judge[tmpi] = True
        #             tmpi += 1
        #
        #
        # print(judge)
        # if judge[-1] is False:
        #     return False
        # else:
        #     return True

        """o(n)"""
        # maxpos = 0
        # for i in range(len(nums)-1):
        #     maxpos = max(maxpos, i + nums[i])
        #     if maxpos == i:
        #         return False
        # return True

        """执行用时最短"""
        length = len(nums)
        if length == 1:
            return True
        steps_require = 1
        i = length - 2
        while i >= 0:
            if nums[i] >= steps_require:
                steps_require = 0
            steps_require += 1
            i -= 1
        return steps_require == 1

print(Solution().canJump([2,3,1,1,4]))
print(Solution().canJump([3,2,1,0,4]))
print(Solution().canJump([2, 0, 0]))
