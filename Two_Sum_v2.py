class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        targets = {}
        
        for i in range(0, len(nums)):
            if nums[i] in targets:
                return [targets[nums[i]], i]
            obj = target - nums[i]
            targets[obj] = i