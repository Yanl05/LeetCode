class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype
        """
        # dp = [0] + [-1]*amount
        # for i in range(amount):
        #     if dp[i] < 0:
        #         continue
        #     for item in coins:
        #         if i + item > amount:
        #             continue
        #         if dp[i+item] < 0 or dp[i+item] > dp[i] + 1:
        #             dp[i+item]=dp[i]+1
        # return dp

        # if amount == 0:
        #     return 0
        # helper = [0x7fffffff]*(amount+1)
        # helper[0] = 0
        # for i in range(amount+1):
        #     for j in coins:
        #         if i-j >= 0 and helper[i-j] != 0x7fffffff:
        #             helper[i] = min(helper[i-j]+1, helper[i])
        # return helper[-1] if helper[-1] != 0x7fffffff else -1

        # 降序
        coins.sort(reverse=True)
        self.result = float('inf')

        def dfs(largest_coin, remainder, used_coins):
            if remainder == 0:
                self.result = min(self.result, used_coins)
            for i in range(largest_coin, len(coins)):
                if remainder >= coins[i]*(self.result-used_coins):
                    break
                if coins[i] <= remainder:
                    dfs(i, remainder-coins[i], used_coins+1)
        dfs(0, amount, 0)
        return self.result if self.result != float('inf') else -1






print(Solution().coinChange([1,2,5], 11))