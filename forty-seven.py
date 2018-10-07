class Solution:
    # def permute(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: List[List[int]]
    #     """
    #     self.res = []
    #     sub = []
    #     self.dfs(nums, sub)
    #     return self.res
    # def dfs(self, Nums, subList):
    #     if len(subList) == len(Nums):
    #         print(self.res, subList)
    #         self.res.append(subList[:])
    #     for m in Nums:
    #         if m in subList:
    #             continue
    #         subList.append(m)
    #         self.dfs(Nums, subList)
    #         subList.remove(m)

    # def permuteUnique(self, nums):
    #     self.res = []
    #     subList = []
    #     # self.used = [False] * len(nums)
    #     self.dfs(nums, subList)
    #     return self.res
    # def dfs(self, nums, subList):
    #     if len(nums) == len(subList):
    #         # print(self.res, subList)
    #         self.res.append(subList[:])
    #     for i in nums:
    #         if i in subList:
    #             continue
    #         # if self.used[i] == True and nums[i] in subList:
    #         #     continue
    #         subList.append(i)
    #         # self.used[i] = True
    #         self.dfs(nums, subList)
    #         subList.remove(i)

    # def permuteUnique(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: List[List[int]]
    #     """
    #     self.res = []
    #     subList = []
    #     self.used = [False] * len(nums)
    #     self.dfs(nums, subList)
    #     return self.res
    #
    # def dfs(self, nums, subList):
    #     if len(subList) == len(nums):
    #         self.res.append(subList[:])
    #     for i in range(len(nums)):
    #         if self.used[i] == True and nums[i] in subList:
    #             continue
    #         subList.append(nums[i])
    #         self.used[i] = True
    #         self.dfs(nums, subList)
    #         subList.remove(nums[i])
    #         self.used[i] = False

    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        我们需要加一个flagList来告诉我们哪个值之前走过，还要记录上一个比如
第一个值 我已经走过一次1了，就不再走1了。
        """
        self.res = []
        sub = []
        nums = sorted(nums)
        fl = [0] * len(nums)
        self.dfs(nums, [], fl)
        return self.res
    def dfs(self, nums, subList, flagList):
        if len(subList) == len(nums):
            self.res.append(subList[:])
        last = None
        for idx in range(len(nums)):
            m = nums[idx]
            if flagList[idx] == 1:
                continue
            if last == m:
                continue
            flagList[idx] = 1
            subList.append(m)
            self.dfs(nums, subList, flagList)
            last = subList.pop()
            flagList[idx] = 0

print(Solution().permuteUnique([1, 1, 2]))
