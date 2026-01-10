class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        rotation = {}
        for i in range(0, len(nums)):
            rotation[(i + k) % len(nums)] = nums[i]
        
        for pos in rotation:
            nums[pos] = rotation[pos]