class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        answer = [1] * len(nums)

        # Compute the prefix, not counting the ith element.
        prefix = 1
        for i in range(0, len(nums)):
            answer[i] = prefix
            prefix *= nums[i]

        # Compute the suffix with the same array used with the prefix, getting the final answer.
        suffix = 1
        for i in range(len(nums) - 1, -1, -1):
            answer[i] *= suffix
            suffix *= nums[i]

        return answer