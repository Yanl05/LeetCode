class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        # tmp = 0
        # ret = 0
        # i = 0
        # lens = len(s)
        # while i < (lens - 1):
        #     while s[i] == '(' and s[i + 1] == ')':
        #         tmp = tmp + 2
        #         i += 2
        #         if i >= lens - 1:
        #             break
        #     if ret < tmp:
        #         ret = tmp
        #     i += 1
        # return ret

        # i, x, y = 0, 0, 0
        # lens = len(s)
        # while i < lens:
        #     if x >= 0 and s[i] == '(':
        #         x += 1
        #
        #     if x != 0 and s[i] == ')':
        #         x -= 1
        #         y += 2
        #     i += 1
        # y = y - (x*2)
        # return y

        ans = 0
        n = len(s)
        stack = []
        st = 0
        for i in range(n):
            if s[i] == '(':
                stack.append(i)
            else:
                if len(stack) == 0:
                    st = i + 1
                    continue
                else:
                    stack.pop()
                    if len(stack) == 0:
                        ans = max(ans, i - st + 1)
                    else:
                        ans = max(ans, i - stack[-1])
                        print(type(i - stack[-1]))
                        print(type(stack[-1]))
        return ans
print(Solution().longestValidParentheses("(()"))
