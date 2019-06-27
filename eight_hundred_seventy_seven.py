# -*- coding: UTF-8 -*-

"""
# @Time    : 2019-06-27 08:53
# @Author  : yanlei
# @FileName: eight_hundred_seventy_seven.py

亚历克斯和李用几堆石子在做游戏。偶数堆石子排成一行，每堆都有正整数颗石子 piles[i] 。

游戏以谁手中的石子最多来决出胜负。石子的总数是奇数，所以没有平局。

亚历克斯和李轮流进行，亚历克斯先开始。 每回合，玩家从行的开始或结束处取走整堆石头。 这种情况一直持续到没有更多的石子堆为止，此时手中石子最多的玩家获胜。

假设亚历克斯和李都发挥出最佳水平，当亚历克斯赢得比赛时返回 true ，当李赢得比赛时返回 false 。

 

示例：

输入：[5,3,4,5]
输出：true
解释：
亚历克斯先开始，只能拿前 5 颗或后 5 颗石子 。
假设他取了前 5 颗，这一行就变成了 [3,4,5] 。
如果李拿走前 3 颗，那么剩下的是 [4,5]，亚历克斯拿走后 5 颗赢得 10 分。
如果李拿走后 5 颗，那么剩下的是 [3,4]，亚历克斯拿走后 4 颗赢得 9 分。
这表明，取前 5 颗石子对亚历克斯来说是一个胜利的举动，所以我们返回 true 。


题解：
当集合中元素大于2时，先选的人从序列两头拿，可以分成两种情况
以ABC为例，可以拿A，剩余BC，后手会选择BC的最佳拿取方式，
所以先手得分为A-BC得分，即：results[i][j]=piles[i]-results[i+1][j]；
也可以拿C，剩余AB，同理有results[i][j]=piles[j]-results[i][j-1]；
选择分值较大的那个即可。上面两个式子都要求我们在求results[i][j]的时候知道
它的下面和左边一个格子的值，所以我们从下到上，从左到右计算填表。

"""


class Solution(object):
    def stoneGame(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """
        dp = [[0 for _ in range(len(piles))] for _ in range(len(piles))]
        for i in range(len(piles)):
            dp[i][i] = piles[i]
        for j in range(1, len(piles)):
            for i in range(j-1, -1, -1):
                dp[i][j]=max(piles[i]-dp[i+1][j], piles[j]-dp[i][j-1])
        return dp[0][-1]>0



print(Solution().stoneGame([3,7,2,3]))
