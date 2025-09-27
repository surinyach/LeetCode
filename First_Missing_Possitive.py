class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = len(nums)
    
        for i in range(0, total):
            n = nums[i]
            if n < 1 or n > total:
                nums[i] = total + 1

        for i in range(0, total):
            n = abs(nums[i])
            if n < total + 1 and nums[n - 1] > 0:
                nums[n - 1] = nums[n - 1] * (-1)
                    
        for i in range(0, total):
            if nums[i] > 0:
                return i + 1
        
        return total + 1