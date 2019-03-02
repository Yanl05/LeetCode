class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        # if not triangle:
        #     return 0
        # lent = len(triangle)
        # ret = triangle[0][0]
        # tmp = 0
        # for i in range(1, lent):
        #     # num = min(triangle[i][tmp], triangle[i][tmp+1])
        #     if triangle[i][tmp] > triangle[i][tmp+1]:
        #         ret += triangle[i][tmp+1]
        #         # print(triangle[i][tmp + 1])
        #         tmp += 1
        #     else:
        #         ret += triangle[i][tmp]
        #         # print(triangle[i][tmp])
        # return ret
        # 创建一个temp列表，从下至上，先把最后一行全部赋给temp，然后其前两位数和上一行的相应位置相加，值放在前两位数的第一个数的位置。（因为后面相加 用不上这个数了）
        # 一直往上推，最小的数，就在temp的第一位
        if not triangle:
            return 0
        if len(triangle) == 1:
            return min(triangle[0])
        temp = [0 for _ in triangle[-1]]
        for i in range(len(triangle)-1, -1, -1):
            for j in range(len(triangle[i])):
                if i == len(triangle)-1:
                    temp[j] = triangle[i][j]
                else:
                    temp[j] = min(temp[j], temp[j+1])+triangle[i][j]
        return temp[0]

print(Solution().minimumTotal(
[[-1],
 [2,3],
 [1,-1,-3]]))