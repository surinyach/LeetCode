class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        min_lenght = float('inf')
        summ = 0
        l = 0

        for r in range(len(nums)):

            summ += nums[r]

            while summ >= target:
                min_lenght = min(min_lenght, r-l+1)
                summ -= nums[l]
                l += 1

        if min_lenght != float('inf'):
            return min_lenght
        
        return 0