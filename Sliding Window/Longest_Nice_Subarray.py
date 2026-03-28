from typing import List

class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        longest = 0
        l = 0
        # bitwise AND is only equal to 0 if all the 1 of the new number are matched with a 0.
        # Then doing bitwise OR through the subsarray elements is assured that if one has a 1 in a position where the new number has it, the chain will break.
        partial_or = 0

        for r in range(0, len(nums)):
            while partial_or & nums[r] != 0:
                partial_or ^= nums[l]
                l += 1

            longest = max(r-l+1, longest)
            partial_or = partial_or | nums[r]
        
        return longest