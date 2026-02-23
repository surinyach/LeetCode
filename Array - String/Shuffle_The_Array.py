class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        new_arr = []
        for i in range(n):
            new_arr.append(nums[i])
            new_arr.append(nums[n + i])
        return new_arr