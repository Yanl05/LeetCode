class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.res = []
        subList = []
        self.dfs(nums, subList)
        return self.res
    def dfs(self, nums, subList):
        if len(nums) == len(subList):
            # print(self.res, subList)
            self.res.append(subList[:])
        for i in nums:
            if i in subList:
                continue
            subList.append(i)
            self.dfs(nums, subList)
            subList.remove(i)
