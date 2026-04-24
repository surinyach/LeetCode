class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        nums.sort()
        max_sequence = 1
        temp_sequence = 1
        for i in range(1, len(nums)):
            if nums[i] - nums[i - 1] == 1:
                temp_sequence += 1
            elif nums[i] != nums[i - 1]:
                max_sequence = max(temp_sequence, max_sequence)
                temp_sequence = 1
        
        return max(temp_sequence, max_sequence)

        # Time Complexity: O(n * log n)
            # Where n is len(nums), and the upper boundary is set by the sort operation
        # Space Complexity: O(1)