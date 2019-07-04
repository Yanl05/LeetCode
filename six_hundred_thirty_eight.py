# -*- coding: UTF-8 -*-

"""
# @Time    : 2019-07-04 09:00
# @Author  : yanlei
# @FileName: six_hundred_thirty_eight.py

在LeetCode商店中， 有许多在售的物品。

然而，也有一些大礼包，每个大礼包以优惠的价格捆绑销售一组物品。

现给定每个物品的价格，每个大礼包包含物品的清单，以及待购物品清单。请输出确切完成待购清单的最低花费。

每个大礼包的由一个数组中的一组数据描述，最后一个数字代表大礼包的价格，其他数字分别表示内含的其他种类物品的数量。

任意大礼包可无限次购买。

示例 1:

输入: [2,5], [[3,0,5],[1,2,10]], [3,2]
输出: 14
解释:
有A和B两种物品，价格分别为¥2和¥5。
大礼包1，你可以以¥5的价格购买3A和0B。
大礼包2， 你可以以¥10的价格购买1A和2B。
你需要购买3个A和2个B， 所以你付了¥10购买了1A和2B（大礼包2），以及¥4购买2A。
示例 2:

输入: [2,3,4], [[1,1,0,4],[2,2,1,9]], [1,2,1]
输出: 11
解释:
A，B，C的价格分别为¥2，¥3，¥4.
你可以用¥4购买1A和1B，也可以用¥9购买2A，2B和1C。
你需要买1A，2B和1C，所以你付了¥4买了1A和1B（大礼包1），以及¥3购买1B， ¥4购买1C。
你不可以购买超出待购清单的物品，尽管购买大礼包2更加便宜。


解题思路：
    回溯法 + 剪枝（利用过滤来剪枝）
"""


class Solution(object):
    def shoppingOffers(self, price, special, needs):
        """
        :type price: List[int]
        :type special: List[List[int]]
        :type needs: List[int]
        :rtype: int
        """
        self.price = price
        # 过滤掉比原价买不划算的礼包
        special = list(filter(lambda x: x[-1] < sum(x[i] * price[i] for i in range(len(price))), special))

        return self.shopping(special, needs)

    def shopping(self, spcial, needs):
        """
        从 spcial中 刚刚好购买needs所需的最低花费

        :param spcial:
        :param needs:
        :return:
        """
        if not needs:
            return 0
        # 先过滤掉 spcial中某一项物品超过needs的礼包
        spcial = list(filter(lambda x: all(x[i] <= needs[i] for i in range(len(needs))), spcial))
        # 如果过滤后为空，则返回直接购买的价格
        if not spcial:
            return sum(self.price[i] * needs[i] for i in range(len(needs)))
        # 回溯
        res = []
        for pac in spcial:
            res.append(pac[-1] + self.shopping(spcial, [needs[i] - pac[i] for i in range(len(needs))]))
            print(res)
        return min(res)


print(Solution().shoppingOffers([2, 5], [[3, 0, 5], [1, 2, 10]], [3, 2]))
