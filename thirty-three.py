class Solution:
    def BinSearch1(self, array, key, low, high):
        mid = int((low + high) // 2)
        if key == array[mid]:  # 若找到
            return mid
        if low > high:
            return '***'

        if key < array[mid]:
            return self.BinSearch1(array, key, low, mid - 1)  # 递归
        if key > array[mid]:
            return self.BinSearch1(array, key, mid + 1, high)

    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if nums == []:
            return -1

        lenn = len(nums)
        st = 0
        if lenn == 1:
            if nums[st] != target:
                return -1
            else:
                return st
        for i in range(1, lenn):
            if nums[i] < nums[0]:
                st = i
                break
        if st == 0:
            ret = Solution().BinSearch1(nums, target, 0, lenn-1)
            if ret != '***':
                return ret
            else:
                return -1

        if target >= nums[0]:
            ret = Solution().BinSearch1(nums[:st], target, 0, st - 1)
            if ret != '***':
                return ret
            else:
                return -1
        else:
            #print(nums[st:])
            ret = Solution().BinSearch1(nums[st:], target, 0, lenn-st-1)
            if ret != '***':
                return ret + st
            else:
                return -1

print(Solution().search([1,3],3))
