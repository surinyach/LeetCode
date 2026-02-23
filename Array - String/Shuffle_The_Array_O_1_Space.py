class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        # Video: Shuffle the Array (Constant Space) - Leetcode 1470 - Python (https://www.youtube.com/watch?v=IvIKD_EU8BY)
        # Bit manipulation technique, taking advantage of the 1 <= nums[i] <= 10^3 condition

        # Generate the x, y pairs
        # x1, y1 ; x2, y2 ... ; xn, yn on the first n - 1 positions of the array
        for i in range(n):
            nums[i] = nums[i] << 10
            nums[i] = nums[i] | nums[i + n]

        # Place the correct x and y values from back to front
        j = len(nums) - 1
        for i in range(n - 1, -1, -1):
            y = nums[i] & (2**10 - 1)
            x = nums[i] >> 10
            nums[j] = y
            nums[j - 1] = x
            j -= 2
        
        return nums