class Solution:
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        #print(candidates)
        self.result = []
        start = 0
        self.backtrack(candidates, target, start, [])
        return self.result
    def backtrack(self, candidates, target, start, val):
        if target == 0 and val not in self.result:
            self.result.append(val[:])
        for i in range(start, len(candidates)):
            if target > 0:
                val.append(candidates[i])
            else:
                break
            self.backtrack(candidates, target - candidates[i], i + 1, val)
            val.pop()
