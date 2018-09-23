class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates = list(set(candidates))  # set 生成无序不重复元素集
        sorted(candidates)  # 排序，返回一个新的list
        self.result = []
        start = 0
        self.backtrack(candidates, target, start, [])
        return self.result
    def backtrack(self, candidates, target, start, val):
        if target == 0:
            self.result.append(val[:])
        for i in range(start, len(candidates)):
            if target > 0:
                val.append(candidates[i])
            else:
                break
            self.backtrack(candidates, target - candidates[i], i, val)
            val.pop()
