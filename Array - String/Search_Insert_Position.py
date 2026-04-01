class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l = 0
        r = len(nums) - 1

        while l <= r:
            middle = (l + r) // 2
            if nums[middle] == target:
                return middle
            elif nums[middle] > target:
                r = middle - 1
            else:
                l = middle + 1
        
        return l