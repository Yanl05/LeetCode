class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        nums.sort()
        for i in range(len(nums)-2):
            if i == 0 or nums[i] > nums[i-1]:  # nums[i] > nums[i-1] 判断nums[i]与nums[i+1]是否相同
                left = i + 1
                right = len(nums) - 1
                while left < right:
                    ident = nums[left] + nums[right] + nums[i]
                    if ident == 0:
                        ans.append([nums[i], nums[left], nums[right]])
                        left += 1; right -= 1
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
                    elif ident < 0:
                        left += 1
                    else:
                        right -= 1
        return ans
