class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        l = 0 
        partial_score = nums[0]
        max_score = nums[0]
        visited = {nums[0]: 0}

        for r in range(1, len(nums)):
            if nums[r] in visited:
                duplicate_index = visited[nums[r]]
                while l <= duplicate_index:
                    partial_score -= nums[l]
                    visited.pop(nums[l])
                    l += 1
            
            visited[nums[r]] = r
            partial_score += nums[r]
            max_score = max(max_score, partial_score)

        return max_score