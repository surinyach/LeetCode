class Solution(object):
    def removeElement(self, nums, val):
        k = 0

        for i in range(0, len(nums)):
            n = nums[i]
            if n == val:
                for j in range(len(nums) - 1, i, -1):
                    n1 = nums[j]
                    if n1 != val:
                        k += 1
                        nums[i] = nums[j]
                        nums[j] = val
                        break
            else:
                k += 1

        return k