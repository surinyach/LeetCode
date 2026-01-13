class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = -200
        k = 0
        for num in nums:
            if num != n:
                n = num
                nums[k] = num
                k += 1
        return k