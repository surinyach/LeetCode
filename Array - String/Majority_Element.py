class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        elements = {}
        target = len(nums) / 2
        for num in nums:
            if num in elements:
                elements[num] += 1
            else:
                elements[num] = 1

            if elements[num] > target:
                return num