class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lenn = len(nums)
        if lenn == 0:
            return 0
        pre = nums[0]
        for i in range(1, lenn):
            if pre == nums[i]:
                nums[i] = '*'
            else:
                pre = nums[i]
        i = 0
        while lenn:
            if nums[i] == '*':
                del nums[i]
            else:
                i += 1
            lenn -=1
        return len(nums)
