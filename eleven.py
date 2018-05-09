class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        lenh = len(height)
        maxarea = 0
        area = 0
        p = 0
        q = lenh - 1
        while p < q:
            area = (q - p) * min(height[p], height[q])
            if maxarea < area:
                maxarea = area
            if height[p] < height[q]:
                p += 1
            else:
                q -= 1
        return maxarea
