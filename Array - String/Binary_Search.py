class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0 
        r = len(nums) - 1
        while l <= r:
            middle = (l + r) // 2
            n = nums[middle]
            if n == target:
                return middle
            elif n > target:
                r = middle - 1
            else:
                l = middle + 1 
        return -1