class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if nums == None:
            return 0
        lenn = len(nums)
        for i in range(lenn):
            if nums[i] == val:
                nums[i] = '*'
        i = 0
        while lenn:
            if nums[i] == '*':
                del nums[i]
            else:
                i += 1
            lenn -=1
        return len(nums)
