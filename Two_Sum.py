class Solution(object):
    def twoSum(self, nums, target):
        solution = []

        # Loop through each element in nums
        for i in range(len(nums)):
            # Iterate through the subsequent elements in nums
            for j in range ((i + 1), len(nums)):
                if nums[i] + nums[j] == target:
                    solution.append(i)
                    solution.append(j)
                    return solution