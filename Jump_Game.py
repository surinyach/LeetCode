class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        max_pos = 0
        for i in range(0, len(nums)):
            if i > max_pos: 
                break
            max_pos = max(nums[i] + i, max_pos)
            if max_pos >= len(nums) - 1:
                return True
        return False