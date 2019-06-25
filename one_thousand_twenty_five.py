# -*- coding: UTF-8 -*-

"""
# @Time    : 2019-06-25 22:53
# @Author  : yanlei
# @FileName: one_thousand_twenty_five.py

爱丽丝和鲍勃一起玩游戏，他们轮流行动。爱丽丝先手开局。

最初，黑板上有一个数字 N 。在每个玩家的回合，玩家需要执行以下操作：

选出任一 x，满足 0 < x < N 且 N % x == 0 。
用 N - x 替换黑板上的数字 N 。

"""

class Solution(object):
    def divisorGame(self, N):
        """
        :type N: int
        :rtype: bool
        """
        target = [0 for _ in range(N+1)]
        target[1] = 0 # alice 抽到1，lose
        if N<=1:
            return False
        else:
            target[2] = 1 # alice 抽到2， win
            for i in range(3, N+1):
                for j in range(1,i//2):
                    if i%j==0 and target[i-j]==0:
                        target[i] = 1
                        break
            return target[N]==1




print(Solution().divisorGame(4))