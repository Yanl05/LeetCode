class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxPro = nums[0]
        minPro = nums[0]
        ret = nums[0]
        for i in range(1, len(nums)):
            t1 = maxPro * nums[i]
            t2 = minPro * nums[i]

            maxPro = max(max(t1, t2), nums[i])
            minPro = min(min(t1, t2), nums[i])

            ret = max(ret, maxPro)
        return ret

        # maxPro = nums[0]
        # ret = nums[0]
        # for num in nums[1:]:
        #     if maxPro<=0:
        #         maxPro = num
        #     else:
        #         maxPro += num
        #     ret = max(ret, maxPro)
        # return ret

print(Solution().maxProduct([-2,1,-3,4,-1,2,1,-5,4]))
