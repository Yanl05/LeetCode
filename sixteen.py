class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        print(nums)

        difmin = 9999999
        ans = 0
        lenn = len(nums)
        for i in range(lenn - 2):
            left = i + 1
            right = lenn - 1
            while left < right:
                count = nums[i] + nums[left] + nums[right] -target

                if count == 0:
                    return target
                else:
                    dif = abs(count)
                    if dif <= difmin:
                        ans = count + target
                        difmin = dif
                    if count + target < target:
                        left += 1
                    else:
                        right -= 1
        return ans
