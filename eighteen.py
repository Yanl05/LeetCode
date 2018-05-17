class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        lenn = len(nums)
        ans = []
        for i in range(lenn - 3):
            for j in range(i + 1, lenn - 2):
                left = j+1
                right = lenn-1
                while left < right:
                    count = nums[i]+nums[j]+nums[left]+nums[right]
                    if count == target:
                        if [nums[i], nums[j], nums[left], nums[right]] not in ans:
                            ans.append([nums[i], nums[j], nums[left], nums[right]])
                            left += 1
                            right -= 1
                        else:
                            left += 1
                            right -= 1
                    elif count < target:
                        left += 1
                    else:
                        right -= 1
        return ans
