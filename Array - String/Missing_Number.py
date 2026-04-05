from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        l = 0
        r = len(nums) - 1
        while l <= r:
            middle = r + l // 2
            n = nums[middle]
            if n <= middle:
                l = middle + 1
            else:
                r = middle - 1
        return l