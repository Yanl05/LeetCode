class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def getret(n, left, right, ret, ans):
            if left + right == 2 * n:
                ans.add(ret)
                return
            if left < n:
                getret(n, left + 1, right, ret + '(', ans)
                if right < left:
                    getret(n, left, right + 1, ret + ')', ans)
            else:
                getret(n, left, right + 1, ret + ')', ans)

        ans = set()
        getret(n, 0, 0, "", ans)

        return list(ans)


print(Solution().generateParenthesis(3))
