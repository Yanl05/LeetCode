import math
class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        lenn = len(nums)
        pos = lenn - 1
        while nums[pos - 1] > nums[pos]:
            pos -= 1
        i = pos
        if pos == 0:
            return nums[::-1]
        y = nums[pos]
        x = nums[pos - 1]
        while i < lenn:
            if i + 1 == lenn:
                tmp = nums[pos - 1]
                nums[pos - 1] = nums[i]
                nums[i] = tmp
                break
            if nums[i] > x and nums[i + 1] < x:
                tmp = nums[pos - 1]
                nums[pos - 1] = nums[i]
                nums[i] = tmp
                break
            i += 1
        # a = nums[lenn:pos - 1:-1]
        # b = nums[0:pos]
        # c = b + a
        hcnt = (lenn-pos)//2
        tmp = 0
        start = pos
        for i in range(hcnt):
            # tmp = nums[i]
            # nums[i] = nums[-(i + 1)]
            # nums[-(i + 1)] = tmp
            tmp = nums[pos + i]
            nums[pos + i] = nums[-(i + 1)]
            nums[-(i + 1)] = tmp
        return nums
        # nums = [5, 4, 7, 5, 3, 2]
        # a = nums[5:1:-1]
        # b = nums[0:2]
        # print(a)
        # print(b)
        # c = b + a
        '''
        i = len(nums) - 1
        while (i > 0) and (nums[i-1] >= nums[i]):
            i -= 1
        temp = nums[i-1]
        j = i
        while (j < len(nums)) and (nums[j] > temp):
            j += 1
        nums[i-1] = nums[j-1]
        nums[j-1] = temp
        nums_part_sorted = sorted(nums[i:])
        nums[i:] = nums_part_sorted
        '''

        #print(nums[0])

print(Solution().nextPermutation([3,2,1]))
