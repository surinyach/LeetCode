class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        triplets = []
        n = len(nums)
        
        for i in range(0, n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            right = n - 1
            left = i + 1
            while left < right:
                sum = nums[i] + nums[left] + nums[right] 
                if sum == 0:
                    triplets.append([nums[i], nums[left], nums[right]])

                    right -= 1
                    left += 1

                    # Avoid duplicates when the same answer is concatenated
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                elif sum < 0:
                    left += 1
                else:
                    right -= 1
        
        return triplets       