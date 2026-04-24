class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = {}
        for i in range(len(nums)):
            n = nums[i]
            if n in seen:
                if abs(i - seen[n]) <= k:
                    return True
                else:
                    seen[n] = i
            else:
                seen[n] = i
        return False
    
    # Time Complexity: O(n), being n the length of nums
    # Space Complexity: O(n), being all the elements in nums in case all of them are different