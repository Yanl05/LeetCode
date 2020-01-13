"""
使用两个数组来存储left   right 的最大柱子高度
用公式
 min(left_max[i], right_max[i]) - height[i]
 来计算当前位置的最大储水两



"""
class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
            return 0
        n = len(height)
        ret = 0
        left_max, right_max = [0] * n, [0] * n
        left_max[0] = height[0]
        for i in range(1, n):
            left_max[i] = max(height[i], left_max[i - 1])
        right_max[n - 1] = height[n - 1]
        for i in range(n - 2, -1, -1):
            right_max[i] = max(height[i], right_max[i + 1])

        for i in range(1, n - 1):
            tmp = min(left_max[i], right_max[i]) - height[i]
            ret += tmp
        return ret


print(Solution().trap([0,1,0,2,1,0,1,3,2,1,2,1]))